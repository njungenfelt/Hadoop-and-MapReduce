#!/usr/bin/python

import sys
import csv

# This reducer gives id, body length, and average length of answer for all forum questions

def Reduce():

	reader = csv.reader(sys.stdin, delimiter='\t')

	answersCount = 0
	answersLength = 0
	lastId = None

	for line in reader:
		if len(line) != 3:
			# Something has gone wrong. Skip this line.
			continue

		thisId = line[0]
		thisType = line[1]
		thisLength = float(line[2])

		if lastId and lastId != thisId:
			MakeOutput(lastId, postLength, answersLength, answersCount)
			lastId = thisId
			answersCount = 0
			answersLength = 0

		lastId = thisId

		if thisType == "answer":
			answersCount += 1
			answersLength += thisLength
		elif thisType == "question":
			postLength = int(thisLength)

	if lastId != None:
		MakeOutput(lastId, postLength, answersLength, answersCount)

def MakeOutput(id, length, answersLength, answersCount):

	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	# To avoid division by zero:
	if answersCount == 0:
		answerAvg = 0
	else:
		answerAvg = answersLength/answersCount

	row = id, length, answerAvg
	writer.writerow(row)

if __name__ == "__main__":
	Reduce()
