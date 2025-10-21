from itertools import repeat

def repeater(seq, n):
    for i in seq:
       for j in repeat(1, n):
           yield j
