def LookSay():
    s = '1'
    while True:
        for c in s:
            yield int(c)
        next_s = ''
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                next_s += str(count) + s[i - 1]
                count = 1
        next_s += str(count) + s[-1]
        s = next_s
