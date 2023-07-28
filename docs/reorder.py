import sys

filename = sys.argv[1]

def reorder(f):
    with open(f, 'r') as ups:
        lines = ups.readlines()
        for line in lines:
            line = line.rstrip()
            if len(line) == 0:
                continue
            tokens = line.split(' --- ')
            if len(tokens) > 1:
                print(f"{tokens[1]:8} {tokens[0]}")
            else:
                print(tokens[0])

reorder(filename)