# master_2016_2017_trump.py
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

	cur3 = conn.cursor()
	cur3.execute("DELETE FROM real_property_master_trump")
	cur3.close()

	cur.execute("SELECT documentid FROM real_property_parties_2016_2017_clean;") # Pull all the document IDs from the real_property_parties_2016_2017_clean table
	records = cur.fetchall() # Put all the results into memory

	for rec in records:
		cur2 = conn.cursor()
		cur2.execute("INSERT INTO real_property_master_trump SELECT * FROM real_property_master_2016_2017 WHERE documentid=%s;", (rec[0],))

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

