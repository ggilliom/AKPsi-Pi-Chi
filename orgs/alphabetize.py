import sys

def getMin(a, b):
	# return length of shorter string
	return min(len(a), len(b))

def isSmaller(org, pivot):
	# return True if org is smaller than pivot, False otherwise
	minLen = getMin(org, pivot)
	print("minLen: " + str(minLen))
	for num in range(minLen):
		'''
		Runtime is based on length of the shorter of two strings: pivot or current org (would affect
		runtime only if all lines have very long names and are spelled the same...little/no
		consistency)
		'''
		print("num: " + str(num))
		if ord(org[num]) < ord(pivot[num]):
			return True
		if ord(org[num]) > ord(pivot[num]):
			return False
	return False

def qsort(lines):
	if len(lines) == 0:
		return lines
	elif len(lines) == 1:
		return lines
	else:
		pivotOrd = ord(lines[0][0])
		bigger = []
		smaller = []
		equal = []
		for org in lines:
			if ord(org[0]) < pivotOrd:
				smaller.append(org)
			if ord(org[0]) > pivotOrd:
				bigger.append(org)
			if ord(org[0]) == pivotOrd:
				if org == lines[0]:
					equal.append(org)
				else:
					print("org: " + org)
					print("pivot: " + lines[0])
					if isSmaller(org, lines[0]):
						smaller.append(org)
					else:
						bigger.append(org)	
		sortSmall = qsort(smaller)
		sortBig = qsort(bigger)
		return sortSmall + equal + sortBig

def writeFileLines(file, lines):
	for line in lines:
		file.write(line + "\n")

def getFileLines(file): # returns lines of a file in list form
	lines = []
	for line in file:
		lines.append(line[:-1])
	return lines

# pass in text file to sort alphabetically as command line arg

filename = sys.argv[-1]
file = open(filename, "r")
lines = getFileLines(file)
file.close()

sortOrgs = qsort(lines)

file = open("sorted.txt", "w+")
writeFileLines(file, sortOrgs)
file.close()