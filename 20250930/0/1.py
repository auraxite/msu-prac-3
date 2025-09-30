def average(a, *args):
    return sum((a,) + args) / (len(args) + 1)

print(average(2,4,5))