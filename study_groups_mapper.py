#!/usr/bin/python

import sys
import csv

# This mapper returns, for all forum posts, the node ID of the original question as key and the user ID as value.

def Map():

	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	reader.next()

	for line in reader:
		if len(line) == 19:
			id = line[0]
			user_id = line[3]
			node_type = line[5]
			parent_id = line[6]
			if node_type == "question":
				row = id, user_id
			else:
				row = parent_id, user_id
			writer.writerow(row)

if __name__ == "__main__":
	Map()
