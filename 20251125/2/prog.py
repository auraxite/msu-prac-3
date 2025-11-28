import sys
import math

program_lines = sys.stdin.read().splitlines()
command_list = []
label_pos = {}
pending_jumps = []

for raw_line in program_lines:
    line = raw_line.lstrip()
    if not line:
        continue

    parts = line.split()
    label = None

    if parts[0].endswith(":"):
        label = parts[0][:-1]
        label_pos[label] = len(command_list)
        parts = parts[1:]

    if not parts:
        continue

    op = parts[0]
    args = parts[1:]

    if op.startswith("if") and len(args) == 3:
        pending_jumps.append(args[2])

    if op == "stop":
        command_list.append((op, args))
        continue

    command_list.append((op, args))

for target in pending_jumps:
    if target not in label_pos:
        sys.exit(0)

vars = {}
program_c = 0

def read_var(name):
    try:
        return float(vars.get(name, 0))
    except:
        return 0.0

program_len = len(command_list)

while 0 <= program_c < program_len:
    op, args = command_list[program_c]

    if op == "stop":
        break

    if op == "store" and len(args) == 2:
        num, dest = args
        try:
            value = float(num)
        except:
            value = 0.0
        vars[dest] = value
        program_c += 1
        continue

    if op in ("add", "sub", "mul", "div") and len(args) == 3:
        a, b, dest = args
        x = read_var(a)
        y = read_var(b)
        try:
            match op:
                case "add": res = x + y
                case "sub": res = x - y
                case "mul": res = x * y
                case "div": res = x / y
        except:
            res = math.inf
        vars[dest] = res
        program_c += 1
        continue

    if op.startswith("if") and len(args) == 3:
        left, right, label = args
        left_val, right_val = read_var(left), read_var(right)

        cond = False
        if op == "ifeq": cond = (left_val == right_val)
        elif op == "ifne": cond = (left_val != right_val)
        elif op == "ifgt": cond = (left_val >  right_val)
        elif op == "ifge": cond = (left_val >= right_val)
        elif op == "iflt": cond = (left_val <  right_val)
        elif op == "ifle": cond = (left_val <= right_val)

        if cond:
            program_c = label_pos[label]
        else:
            program_c += 1
        continue

    if op == "out" and len(args) == 1:
        print(read_var(args[0]))
        program_c += 1
        continue

    program_c += 1
