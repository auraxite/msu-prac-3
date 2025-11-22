import sys

data = sys.stdin.buffer.read()
if not data:
    exit(0)

N = data[0]
if N == 0:
    sys.stdout.buffer.write(data)
    exit(0)
first_byte = data[:1]
tail = data[1:]
L = len(tail)

parts = []
for i in range(N):
    start = int(i * L / N)
    end = int((i + 1) * L / N)
    parts.append(tail[start:end])
parts.sort()

sorted_tail = b"".join(parts)
sys.stdout.buffer.write(first_byte + sorted_tail)
