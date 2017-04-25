# related_parties.py
# Run through query using another table as a query conditional.
# Append new query results to a new table

from __future__ import absolute_import, print_function, unicode_literals

import sys # Req'd if command line arguments are used later
import psycopg2
import time

# Connect to tcount
conn = psycopg2.connect(database="acris", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

def query_related_parties():
	"""Script to use table data as the input to another conditional query in postgres.
	Later this could be modified to allow user to designate the source table and column using command line args or similar.
	This version is effectively hardcoded.
	"""
	# Time elapsed debugging
	start = time.time()

	cur.execute("SELECT documentid FROM trump_parties;") # Pull all the document IDs from the trump_related_parties table
	records = cur.fetchall() # Put all the results into memory

	# for rec in records:
	# 	#print("document ID = ", rec[0], "\n") # Debug print

	# 	cur2 = conn.cursor()
	# 	cur2.execute("INSERT INTO trump_related_parties SELECT * FROM real_property_parties WHERE documentid=%s;", (rec[0],))

	i = 0 # Iterator for limiting the number of records queried
	for rec in records:
		#print("document ID = ", rec[0], "\n") # Debug print
		if i == 3:
			break
		cur2 = conn.cursor()
		cur2.execute("INSERT INTO trump_related_parties SELECT * FROM real_property_parties WHERE documentid=%s;", (rec[0],))
		i += 1

	conn.commit()

	cur.close()
	cur2.close()
	conn.close()

	end = time.time()
	print("Time elapsed: ", end - start)
	
if __name__ == '__main__':
	print("Starting...")
	query_related_parties()
	print("Completed")

