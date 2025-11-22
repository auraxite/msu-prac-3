import sys

def to_int(b):
    return int.from_bytes(b, 'little')

try:
    f = sys.stdin.buffer.read()
    if (f[:4] != b'RIFF'):
        raise Exception
    print(f"Size={to_int(f[4:8])}", f"Type={to_int(f[20:22])}", f"Channels={to_int(f[22:24])}", f"Rate={to_int(f[24:28])}", f"Bits={to_int(f[34:36])}", f"Data size={to_int(f[40:44])}", sep = ", ")
except:
    exit(0)