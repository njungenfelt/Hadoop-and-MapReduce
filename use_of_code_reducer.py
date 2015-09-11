#!/usr/bin/python

import sys
import csv

# This reducer prints node type and the percenteage of that node tag that have used <code>

def Reduce():

	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	codeCount = 0
	totalCount = 0
	lastType = None

	for line in reader:
		if len(line) != 2:
			# Something has gone wrong. Skip this line.
			continue

		thisType = line[0]
		thisCount = int(line[1])

		if lastType and lastType != thisType:
			percCode = 100*codeCount/totalCount
			row = lastType, str(percCode) + "%"
			writer.writerow(row)
			lastType = thisType
			codeCount = 0
			totalCount = 0

		lastType = thisType
		codeCount += thisCount
		totalCount += 1

	if lastType != None:
		percCode = 100*codeCount/totalCount
		row = lastType, str(percCode) + "%"
		writer.writerow(row)

if __name__ == "__main__":
	Reduce()
