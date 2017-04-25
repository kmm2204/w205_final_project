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

