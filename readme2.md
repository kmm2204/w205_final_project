Trust in Trump

w205 Final Project

4/25/17

Krista Mar, Riley Rustad, Alex Lau

Summary

New York City maintains an open data repository related to city governance at the website https://opendata.cityofnewyork.us/. One of the data sources stored here is from the city's Automated City Register Information System (ACRIS) database, which stores a large amount of property transactions from four of the city's boroughs (Manhattan, Queens, Bronx, and Brooklyn) for the period 1966 to the present. Recently the businessman and real estate mogul Donald Trump was elected President of the United States. Conflicts of interest issues were raised concerning his vast business apparatus and real estate holdings and how the the far-reaching power of his office might be abused for self-gain. To begin mitigating some of these concerns, Trump announced the creation of a revocable trust which would hold and control his real estate properties while in office. (It should be noted that because his family and close colleagues are the trustees, the COI mitigation qualities of this trust are up for debate.) Using different data sources within ACRIS, we began to examine whether this Trump promise is being kept and what COI issues may or may not be addressed through this trust.

Analysis & Results

ACRIS Real Estate Data

### Preprocessing

### We downloaded some files to our desktop

real-property-masters.csv 
https://data.cityofnewyork.us/api/views/bnx9-e6tj/rows.csv?accessType=DOWNLOAD

real-property-parties.csv 
https://data.cityofnewyork.us/api/views/636b-3b5g/rows.csv?accessType=DOWNLOAD


### Clean up files

We stripped the commas out of the original files as this caused problems later on, since having fields with commas in them were causing inconsistencies. You can see the scripts here.

https://github.com/kmm2204/w205_final_project/blob/master/Analysis/RPM_strip.ipynb
https://github.com/kmm2204/w205_final_project/blob/master/Analysis/RPP_strip.ipynb

Then we uploaded the files to s3


### Uploaded the cleaned files to s3

connect to your ec2 instance
navigate into your /data directory and run the following commands

wget -O real-property-parties.csv	https://s3.amazonaws.com/w205final123/RPM_clean.csv 
wget -O real-property-master.csv https://s3.amazonaws.com/w205final123/RPP_clean.csv


### Using pyspark to parse our files

connect to hadoop
start pyspark

from pyspark import SparkContext

sc = SparkContext()

prop = sc.textFile("file:///data/real-property-parties.csv")

no_head_prop = prop.zipWithIndex().filter(lambda (row,index): index > 0).keys()

not_trump = ["TRUMPET", "STRUMPFLER", "STRUMPF", "TRUMPY", "TRUMPER", "TRUMPF"]

def trump_filter(x):
	if "TRUMP" in x:
		for name in not_trump:
			if name in x:
				return False
			else:
				return True
	else:
		return False

prop_trump = no_head_prop.filter(trump_filter)

def splitter(x):
	tmp = x.split(",")
	return (tmp[0],tmp[1:])

prop_trump_tuples = prop_trump.map(splitter)

master = sc.textFile("file:///data/real-property-master.csv")

no_head_master = master.zipWithIndex().filter(lambda (row,index): index > 0).keys()

master_tuples = no_head_master.map(splitter)

merged = prop_trump_tuples.leftOuterJoin(master_tuples)

def combine(x):
	return (x[0], x[1][0]+x[1][1])

cleaned_merge = merged.map(combine)

cleaned_merge.saveAsTextFile('file:///data/merged_trump_and_master')


### parse connections file in pysparse

from pyspark import SparkContext

sc = SparkContext()

prop = sc.textFile("file:///data/real-property-parties.csv")

no_head_prop = prop.zipWithIndex().filter(lambda (row,index): index > 0).keys()

not_trump = ["TRUMPET", "STRUMPFLER", "STRUMPF", "TRUMPY", "TRUMPER", "TRUMPF"]

def trump_filter(x):
	if "TRUMP" in x:
		for name in not_trump:
			if name in x:
				return False
			else:
				return True
	else:
		return False

prop_trump = no_head_prop.filter(trump_filter)

def splitter(x):
	tmp = x.split(",")
	return (tmp[0],tmp[1:])

prop_trump_tuples = prop_trump.map(splitter)

trump_transaction_ids = prop_trump_tuples.map(lambda x: (x[0],[]))

prop_tuples = no_head_prop.map(splitter)

merged = trump_transaction_ids.join(prop_tuples)

def combine(x):
	return (x[0], x[1][0]+x[1][1])

cleaned_merge = merged.map(combine)

cleaned_merge.saveAsTextFile('file:///data/trump_connections')

### Exit pyspark and combine files


cat /data/trump_connections/* > /data/trump_connections.csv
rm -rf /data/trump_connections/

cat /data/merged_trump_and_master/* > /data/merged_trump_and_master.csv
rm -rf /data/merged_trump_and_master/

### Analysis 

