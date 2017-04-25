# Trust in Trump

# w205 Final Project

## 4/25/17

## Krista Mar, Riley Rustad, Alex Lau

## Summary

New York City maintains an open data repository related to city governance at the website https://opendata.cityofnewyork.us/. One of the data sources stored here is from the city's Automated City Register Information System (ACRIS) database, which stores a large amount of property transactions from four of the city's boroughs (Manhattan, Queens, Bronx, and Brooklyn) for the period 1966 to the present. Recently the businessman and real estate mogul Donald Trump was elected President of the United States. Conflicts of interest issues were raised concerning his vast business apparatus and real estate holdings and how the the far-reaching power of his office might be abused for self-gain. To begin mitigating some of these concerns, Trump announced the creation of a revocable trust which would hold and control his real estate properties while in office. (It should be noted that because his family and close colleagues are the trustees, the COI mitigation qualities of this trust are up for debate.) Using different data sources within ACRIS, we began to examine whether this Trump promise is being kept and what COI issues may or may not be addressed through this trust.

## Analysis & Results

ACRIS Real Estate Data

### Preprocessing

### We downloaded some files to our desktop
```
real-property-masters.csv 
https://data.cityofnewyork.us/api/views/bnx9-e6tj/rows.csv?accessType=DOWNLOAD

real-property-parties.csv 
https://data.cityofnewyork.us/api/views/636b-3b5g/rows.csv?accessType=DOWNLOAD
```

### Clean up files

We stripped the commas out of the original files as this caused problems later on, since having fields with commas in them were causing inconsistencies. You can see the scripts here.

https://github.com/kmm2204/w205_final_project/blob/master/Analysis/RPM_strip.ipynb
https://github.com/kmm2204/w205_final_project/blob/master/Analysis/RPP_strip.ipynb

Then we uploaded the files to s3


### Uploaded the cleaned files to s3

connect to your ec2 instance
navigate into your /data directory and run the following commands

wget -O real-property-parties.csv https://s3.amazonaws.com/w205final123/RPM_clean.csv 

wget -O real-property-master.csv https://s3.amazonaws.com/w205final123/RPP_clean.csv

### Download scripts from repo

wget -O https://github.com/kmm2204/w205_final_project.git

### Run Pyspark Scripts

Download scripts into /data directory

These scripts take the ACRIS data, and isolate the Trump transactions and Trumps connections. It should be noted that it dumps these merged datasets into directories in many parts.

The two main files analyzed are real_property_parties.csv and real_property_master.csv, which  contains information about the people involved with each transaction and the transaction metadata respectively.

spark_parse.py - takes all of the transactions that Trump is associated with, and joins it to the transaction metadata

spark_parse_connections.py - takes the transaction IDs that Trump is assiciated with, and finds the other parties associated with those IDs.

pyspark data/spark_parse.py

pyspark data/spark_parse_connections.py

### Run Cleanup Script
This script takes those many parts from the previous step, and combines them into single csv files.

cleanup.sh

### Analysis 


