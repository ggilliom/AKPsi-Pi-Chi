import sys

def getFileLines(file): # returns lines of a file in list form
	lines = []
	for line in file:
		lines.append(line[:-1])
	return lines

filename = sys.argv[-1] ## Requires command line argument of filename

file = open(filename, "r")

lines = getFileLines(file)

file.close()

print(lines)

dashes = []

for line in lines:
	dashes.append(line.replace(" ", "-"))

print(dashes)

file = open(filename, "w")

for line in dashes:
	file.write(line + "\n")