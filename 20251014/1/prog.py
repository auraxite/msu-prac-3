s = input().lower()

pairs = set()
for i in range(len(s) - 1):
    if s[i].isalpha() and s[i + 1].isalpha():
        pairs.add(s[i] + s[i + 1])

print(len(pairs))
# print(pairs)