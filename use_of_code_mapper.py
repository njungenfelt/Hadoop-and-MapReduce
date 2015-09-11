#!/usr/bin/python

import sys
import csv
import re

# This mapper extracts node_type and whether <code> has been used or not (1/0).

def Map():

	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	reader.next()

	for line in reader:
		if len(line) == 19:
			body = line[4]
			node_type = line[5]
			codeTags = re.findall(r'<code>', body)
			hasCode = int(len(codeTags) >= 1)
			row = node_type, hasCode
			writer.writerow(row)

if __name__ == "__main__":
	Map()
