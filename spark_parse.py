from pyspark import SparkContext

sc = SparkContext()

prop = sc.textFile("file:///data/acris-download/data/real_property_parties.csv")

no_head_prop = prop.zipWithIndex().filter(lambda (row,index): index > 0).keys()

not_trump = ["TRUMPET", "STRUMPFLER", "STRUMPF", "TRUMPY", "TRUMPER", "TRUMPF"]

def trump_filter(x):
	if "TRUMP" in x and x not in not_trump:
		return True
	else:
		return False

prop_trump = no_head_prop.filter(trump_filter)

def spliter(x):
	tmp = x.split(",")
	return (tmp[0],tmp[1:])

prop_trump_tuples = prop_trump.map(spliter)

master = sc.textFile("file:///data/acris-download/data/real_property_master.csv")

no_head_master = master.zipWithIndex().filter(lambda (row,index): index > 0).keys()

master_tuples = no_head_master.map(spliter)

merged = prop_trump_tuples.leftOuterJoin(master_tuples)

def combine(x):
	return (x[0], x[1][0]+x[1][1])

cleaned_merge = merged.map(combine)

cleaned_merge.saveAsTextFile('/data/merged_Trump_and_Master')
