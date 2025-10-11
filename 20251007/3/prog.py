first = input()
w = len(first) - 2
h = 0
water = 0

while True:
    line = input()
    air_c = line.count('.')
    water_c = line.count('~')
    if air_c + water_c == 0:
        break
    h += 1
    water += water_c

air = w * h - water

if h != 0:
    water_layers = water // h
    if water % h > 0:
        water_layers = water // h + 1
else:
    water_layers = 0

w, h = h, w
print("#" * (w + 2))
for i in range(h - water_layers):
    print(f"#{"." * w}#")
for i in range(water_layers):
    print(f"#{"~" * w}#")
print("#" * (w + 2))

if air == 0:
    air_len = 0
    if water == 0:
        str_len = 1
        water_len = 0
    else:
        str_len = len(str(water))
        water_len = 20
elif water == 0:
    str_len = len(str(air))
    water_len = 0
    air_len = 20
elif air > water:
    str_len = len(str(air))
    air_len = 20
    water_len = round(water / air * 20)
else:
    str_len = len(str(water))
    water_len = 20
    air_len = round(air / water * 20)

print("." * air_len, " " * (20 - air_len + 1), f"{air:{str_len}}/{w * h}", sep = "")
print("~" * water_len, " " * (20 - water_len + 1), f"{water:{str_len}}/{w * h}", sep = "")