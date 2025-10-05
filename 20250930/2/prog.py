def sub(obj1, obj2):
    if isinstance(obj1, (int, float)):
        return obj1 - obj2
    else:
        res = [el for el in obj1 if el not in obj2]
        return type(obj1)(res)

print(sub(*eval(s))) if (s := input().strip()) else None

# print(sub(123, 45))
# 78

# print(sub((4,2,7,4,6,87,7), (2,54,67,3,2)))
# (4, 7, 4, 6, 87, 7)

# print(sub(["Q", "WE", "RTY"], ["WE", "ZZ"]))
# ['Q', 'RTY']