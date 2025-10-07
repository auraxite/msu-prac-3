max_len_bin = len(hex(23))
max_len_hax = len(hex(23))

for i in range(12, 24):
    print(f"{bin(i):<{max_len_bin}23} = {hex(i):{max_len_hax}}")