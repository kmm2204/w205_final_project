# Trust in Trump
### w205 Final Project
### 4/25/17
### Krista Mar, Riley Rustad, Alex Lau

## Summary
New York City maintains an open data repository related to city governance at the website https://opendata.cityofnewyork.us/. One of the data sources stored here is from the city's Automated City Register Information System (ACRIS) database, which stores a large amount of property transactions from four of the city's boroughs (Manhattan, Queens, Bronx, and Brooklyn) for the period 1966 to the present. Recently the businessman and real estate mogul Donald Trump was elected President of the United States. Conflicts of interest issues were raised concerning his vast business apparatus and real estate holdings and how the the far-reaching power of his office might be abused for self-gain. To begin mitigating some of these concerns, Trump announced the creation of a revocable trust which would hold and control his real estate properties while in office. (It should be noted that because his family and close colleagues are the trustees, the COI mitigation qualities of this trust are up for debate.) Using different data sources within ACRIS, we began to examine whether this Trump promise is being kept and what COI issues may or may not be addressed through this trust.

## Analysis & Results

### ACRIS Real Estate Data
We started with downloading different ACRIS data tables directly to our AWS VMs. Warning: running the bash commands below will start a process of downloading approximately 7 GB+ of data!
```
wget -O subterranean-rights.csv https://data.cityofnewyork.us/api/views/56kn-pnny/rows.csv?accessType=DOWNLOAD
wget -O real-property-legals.csv https://data.cityofnewyork.us/api/views/8h5j-fqxa/rows.csv?accessType=DOWNLOAD
wget -O real-property-masters.csv https://data.cityofnewyork.us/api/views/bnx9-e6tj/rows.csv?accessType=DOWNLOAD
wget -O real-property-parties.csv https://data.cityofnewyork.us/api/views/636b-3b5g/rows.csv?accessType=DOWNLOAD
wget -O real-property-references.csv https://data.cityofnewyork.us/api/views/pwkr-dpni/rows.csv?accessType=DOWNLOAD
wget -O real-property-remarks.csv https://data.cityofnewyork.us/api/views/9p4w-7npp/rows.csv?accessType=DOWNLOAD
wget -O state-codes.csv https://data.cityofnewyork.us/api/views/5c9e-33xj/rows.csv?accessType=DOWNLOAD
wget -O document-control-codes.csv https://data.cityofnewyork.us/api/views/7isb-wh4c/rows.csv?accessType=DOWNLOAD
wget -O property-types-codes.csv https://data.cityofnewyork.us/api/views/94g4-w6xz/rows.csv?accessType=DOWNLOAD
wget -O personal_property_legals.csv https://data.cityofnewyork.us/api/views/uqqa-hym2/rows.csv?accessType=DOWNLOAD
wget -O personal_property_parties.csv https://data.cityofnewyork.us/api/views/nbbg-wtuz/rows.csv?accessType=DOWNLOAD
wget -O personal_property_master.csv https://data.cityofnewyork.us/api/views/sv7x-dduq/rows.csv?accessType=DOWNLOAD
```

### Hadoop First
With the data downloaded on the VM, we opened up the metastore and began creating the appropriate HDFS directories to hold our files. This allowed us to use a variety of ways to query our data through pyspark, sparkSQL, and Hive.
```
# Create hdfs directory
hdfs dfs -mkdir /user/w205/final/data/subterranean_rights
hdfs dfs -mkdir /user/w205/final/data/real_property_legals
hdfs dfs -mkdir /user/w205/final/data/real_property_masters
hdfs dfs -mkdir /user/w205/final/data/real_property_parties
hdfs dfs -mkdir /user/w205/final/data/real_property_references
hdfs dfs -mkdir /user/w205/final/data/real_property_remarks
hdfs dfs -mkdir /user/w205/final/data/state_codes
hdfs dfs -mkdir /user/w205/final/data/document_control_codes
hdfs dfs -mkdir /user/w205/final/data/property_types_codes
hdfs dfs -mkdir /user/w205/final/data/personal_property_legals
hdfs dfs -mkdir /user/w205/final/data/personal_property_parties
hdfs dfs -mkdir /user/w205/final/data/personal_property_master

## Load data into hdfs
hdfs dfs -put /user/w205/final/data/subterranean_rights subterranean-rights.csv
hdfs dfs -put /user/w205/final/data/real_property_legals real-property-legals.csv
hdfs dfs -put /user/w205/final/data/real_property_masters real-property-masters.csv
hdfs dfs -put /user/w205/final/data/real_property_parties real-property-parties.csv
hdfs dfs -put /user/w205/final/data/real_property_references real-property-references.csv
hdfs dfs -put /user/w205/final/data/real_property_remarks real-property-remarks.csv
hdfs dfs -put /user/w205/final/data/state_codes state_codes.csv
hdfs dfs -put /user/w205/final/data/document_control_codes document_control_codes.csv
hdfs dfs -put /user/w205/final/data/property_types_codes property_types_codes.csv
hdfs dfs -put /user/w205/final/data/personal_property_legals personal_property_legals.csv
hdfs dfs -put /user/w205/final/data/personal_property_parties personal_property_parties.csv
hdfs dfs -put /user/w205/final/data/personal_property_master personal_property_master.csv
```

### PostgreSQL for Speed

## Conclusion

