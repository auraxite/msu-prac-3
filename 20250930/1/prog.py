def Pareto(*pairs):
    res = ()
    for p1 in pairs:
        for p2 in pairs:
            if (p1[0] <= p2[0]) and (p1[1] <= p2[1]) and (p1[0] < p2[0] or p1[1] < p2[1]):
                break
        else:
            res += (p1,)

    return res

print(Pareto(*(eval(input()))))