#!/usr/bin/python

import sys
import csv

# This reducer makes a top 10 list of forum question tags (number of times used)

def Reduce():

	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	tagCount = 0
	lastTag = None
	top10 = []

	for line in reader:
		if len(line) != 2:
			# Something has gone wrong. Skip this line.
			continue

		thisTag = line[0]
		thisCount = line[1]

		if lastTag and lastTag != thisTag:
			row = lastTag, tagCount
			top10.append(row)
			top10 = sorted(top10, key=lambda row: row[1], reverse=True)[:10]
			lastTag = thisTag
			tagCount = 0

		lastTag = thisTag
		tagCount += int(thisCount)

	if lastTag != None:
		row = lastTag, tagCount
		top10.append(row)
		top10 = sorted(top10, key=lambda row: row[1], reverse=True)[:10]

	for row in top10:
		writer.writerow(row)

if __name__ == "__main__":
	Reduce()
