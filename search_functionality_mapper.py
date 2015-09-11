#!/usr/bin/python

import sys
import csv
import re

#This mapper extracts words from forum bodies (key) and post ID they were used in (value)

def Map():

	reader = csv.reader(sys.stdin, delimiter='\t', quoting=csv.QUOTE_ALL)
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	reader.next()
    
	for line in reader:
		if len(line) == 19:
			body = re.findall(r"[\w']+", line[4].lower())
			id = line[0]
			for word in body:
				row = word.replace("'",""), id
				writer.writerow(row)

if __name__ == "__main__":
	Map()
