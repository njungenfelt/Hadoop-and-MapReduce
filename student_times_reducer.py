#!/usr/bin/python

import sys
import csv

# This reducer gives the most frequent hour of posting for each user.

def Reduce():

	reader = csv.reader(sys.stdin, delimiter='\t')

	counts = [0] * 24
	lastUser = None

	for line in reader:
		if len(line) != 2:
			# Something has gone wrong. Skip this line.
			continue

		thisUser = line[0]
		thisHour = int(line[1])

		if lastUser and lastUser != thisUser:
			MakeOutput(lastUser, counts)
			lastUser = thisUser
			counts = [0] * 24

		lastUser = thisUser
		counts[thisHour] += 1


	if lastUser != None:
		MakeOutput(lastUser, counts)

def MakeOutput(user, counts):

	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	# All hours that have the maximum count of posts from the user:
	maxHours = [i for i, j in enumerate(counts) if j == max(counts)]
	for hour in maxHours:
		row = user, hour
		writer.writerow(row)

if __name__ == "__main__":
	Reduce()	
