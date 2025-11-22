import sys

txt = sys.stdin.read()
data = txt.encode("latin1", errors="replace")
res = data.decode("cp1251", errors="replace")
sys.stdout.write(res)