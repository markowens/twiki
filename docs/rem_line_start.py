import sys

filename = sys.argv[1]

def rem_start(f):
    with open(f, 'r') as ups:
        lines = ups.readlines()
        for line in lines:
            line = line.rstrip()
            if len(line) == 0:
                continue
            #tokens = lines.split(")")
            print(line[9:] + " --- " + line[:9])

rem_start(filename)


