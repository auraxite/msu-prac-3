import sys

with open(sys.argv[2], 'w+') as fileOut:
    with open(sys.argv[1], 'w+') as fileIn:
        data = fileIn.readlines()
        print(*sorted(data), file = fileOut)