def manyfor(order, *sequences):
    iters = [iter(seq) for seq in sequences]
    for i in order:
        if not (0 <= i < len(iters)):
            return
        try:
            yield next(iters[i])
        except StopIteration:
            return

# print("".join(manyfor((1, 0, 2) * 16, "ae kha-kha", "Mnsatm", "nrme noob")))
