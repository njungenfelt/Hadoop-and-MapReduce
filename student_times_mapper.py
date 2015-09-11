#!/usr/bin/python

import sys
import csv
from datetime import datetime

# This mapper extracts from each post the ID of the author and the hour during which the post was added.

def Map():

	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	reader.next()

	for line in reader:
		if len(line) == 19:
			author_id = line[3]
			added_at = line[8]
			hour = datetime.strptime(added_at, "%Y-%m-%d %H:%M:%S.%f+00").hour
			row = author_id, hour
			writer.writerow(row)

if __name__ == "__main__":
	Map()
