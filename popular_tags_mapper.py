#!/usr/bin/python

import sys
import csv
import re

# This mapper returns all tags appeared in forum questions and a '1' (for counting)

def Map():

	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	reader.next()

	for line in reader:
		if len(line) == 19:
			tagnames = re.findall(r"[\w']+", line[2])
			node_type = line[5]
			if node_type == "question":
				for tag in tagnames:
					row = tag.lower(), 1
					writer.writerow(row)
			else:
				continue
			
if __name__ == "__main__":
	Map()
