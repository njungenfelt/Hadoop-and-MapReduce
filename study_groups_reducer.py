#!/usr/bin/python

import sys
import csv

# This reducer writes question ID followed by all user IDs connected to that post (question, answer or comment).

def Reduce():

	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	users = []
	lastId = None

	for line in reader:
		if len(line) != 2:
			# Something has gone wrong. Skip this line.
			continue

		thisId = line[0]
		thisUser = line[1]

		if lastId and lastId != thisId:
			row = lastId, users
			writer.writerow(row)
			lastId = thisId
			users = []

		lastId = thisId

		users.append(thisUser)

	if lastId != None:
		row = lastId, users
		writer.writerow(row)

if __name__ == "__main__":
	Reduce()
