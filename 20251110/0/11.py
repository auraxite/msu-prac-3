class A: pass
class B: pass

class C(A, B): pass
class D(B, A): pass

c = 0
for class1 in [A,B,C,D]:
    for class2 in [A,B,C,D]:
        if C not in [class1, class2]:
            continue
        try:
            class E(class1, class2):
                pass
            e = E()
            c += 1
            print(class1, class2)
        except:
            continue

print(c)