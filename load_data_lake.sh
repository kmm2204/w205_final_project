
#load_data_lake.sh

#navigate into directory
cd /data
cd acris-download
cd data

#strip headers
tail -n +2 "country_codes.csv" > countrycodes
tail -n +2 "real_property_master.csv" > realproperty
tail -n +2 "document_control_codes.csv" > documentcontrolcodes
tail -n +2 "real_property_parties.csv" > realpropertyparties
tail -n +2 "property_type_codes.csv" > propertytypecodes
tail -n +2 "real_property_parties_old.csv" > realpropertypartiesold
tail -n +2 "real_property_legals.csv" > realpropertylegals
tail -n +2 "ucc_collateral_codes.csv" > ucccollateralcodes

#make directories in hdfs
hdfs dfs -mkdir /user/w205/final-project/
hdfs dfs -mkdir /user/w205/final-project/data
hdfs dfs -mkdir /user/w205/final-project/data/countrycodes
hdfs dfs -mkdir /user/w205/final-project/data/documentcontrolcodes
hdfs dfs -mkdir /user/w205/final-project/data/realpropertyparties
hdfs dfs -mkdir /user/w205/final-project/data/realpropertypartiesold
hdfs dfs -mkdir /user/w205/final-project/data/realpropertylegals
hdfs dfs -mkdir /user/w205/final-project/data/ucccollateralcodes

#move the files to hdfs
hfs dfs -put /data/acris-download/data
hdfs dfs -put /data/acris-download/data/countrycodes.csv /user/w205/final-project/data/countrycodes
hdfs dfs -put /data/acris-download/data/documentcontrolcodes.csv /user/w205/final-project/data/documentcontrolcodes
hdfs dfs -put /data/acris-download/data/realpropertyparties.csv /user/w205/final-project/data/realpropertyparties
hdfs dfs -put /data/acris-download/data/realpropertypartiesold.csv /user/w205/final-project/data/realpropertypartiesold
hdfs dfs -put /data/acris-download/data/realpropertylegals.csv /user/w205/final-project/data/realpropertylegals
hdfs dfs -put /data/acris-download/data/ucccollateralcodes.csv /user/w205/final-project/data/ucccollateralcodes
