#!/usr/bin/python

import sys
import csv

# This mapper extacts id (if node_type is "question"), parent_id (if node_type is "answer"), node_type and length of body for all posts that are either questions or answers.

def Map():

	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	reader.next()

	for line in reader:
		if len(line) == 19:
			id = line[0]
			body = line[4]
			node_type = line[5]
			parent_id = line[6]
			if node_type == "question":
				row = id, node_type, len(body)
			elif node_type == "answer":
				row = parent_id, node_type, len(body)
			else:
				continue
			writer.writerow(row)

if __name__ == "__main__":
	Map()
