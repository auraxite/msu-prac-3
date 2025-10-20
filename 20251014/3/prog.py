import re
from collections import Counter

W = int(input().strip())
lines = []

while True:
    try:
        line = input()
        if not line.strip():
            break
        lines.append(line)
    except EOFError:
        break

txt = ' '.join(lines).lower()
txt = re.sub(r'[^a-zа-яё]', ' ', txt)
words = txt.split()
new_txt = [x for x in words if len(x) == W]

if new_txt:
    c = Counter(new_txt)
    m = max(c.values())
    result = sorted([w for w, n in c.items() if n == m])
    print(' '.join(result))
