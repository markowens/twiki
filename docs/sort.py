import sys

filename = sys.argv[1]

x = 1


def sort_puns(f):
	with open(f, 'r') as puns:
		lines = puns.readlines()
		lines.sort()
		for line in lines:
			print(line.strip())

def detab(filename):
	with open(filename, 'r') as inputFile:
		for line in inputFile:
			new_line = line.replace('\t', ' ')
			print(new_line.strip())
			
def format_puns(filename):
	with open(filename, 'r') as puns:
		lines = puns.readlines()
		for line in lines:
			tokens = line.split()
			if len(tokens) == 0:
				print("")
			else:
				newline = ' '.join(tokens[1:])
				print("%-8s %s" % (tokens[0], newline))
						


if x == 1:
	sort_puns(filename)
	
if x == 2:
	detab(filename)
	
if x == 3:
	format_puns(filename)	

	




		
		
