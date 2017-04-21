CREATE TABLE IF NOT EXISTS real_properties_parties(
documentid string,
recordtype string,
partytype string,
name string,
address1 string,
address2 string,
country string,
city string,
state string,
zip string,
goodthroughdate string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/w205/final/data/real_property_parties';

CREATE TABLE IF NOT EXISTS trump_transactions(
documentid string,
recordtype string,
partytype string,
name string,
address1 string,
address2 string,
country string,
city string,
state string,
zip string,
goodthroughdate string);

INSERT INTO trump_transactions SELECT * FROM real_properties_parties WHERE name LIKE '%TRUMP%';

SELECT * FROM real_properties_parties WHERE documentid='2003021600161004';