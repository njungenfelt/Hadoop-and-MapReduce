#!/usr/bin/python

import sys
import csv
import re
# To avoid _csv.Error: field larger than field limit (131072)
csv.field_size_limit(sys.maxsize)

# This reducer also works a combiner. It outputs a word and all the posts it has been used in.

def Reduce():

	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	posts = []
	lastWord = None

	for line in reader:
		if len(line) != 2:
			# Something has gone wrong. Skip this line.
			continue

		thisWord = line[0]
		# Map all IDs as integers
		thisPost = map(int, re.findall(r"\d+", line[1]))

		if lastWord and lastWord != thisWord:
			# Flatten 'posts' to avoid "list of lists".
			posts = [val for sublist in posts for val in sublist]
			row = lastWord, posts
			writer.writerow(row)
			lastWord = thisWord
			posts = []

		lastWord = thisWord

		posts.append(thisPost)
		

	if lastWord != None:
		# Flatten 'posts' to avoid "list of lists".
		posts = [val for sublist in posts for val in sublist]
		row = lastWord, posts
		writer.writerow(row)

if __name__ == "__main__":
	Reduce()
