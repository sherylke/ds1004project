#!/usr/bin/env python

import sys
from csv import reader
from pyspark import SparkContext

sc = SparkContext()

csvfile = sc.textFile(sys.argv[1], 1)

def remove_header(itr_index, itr):
	return iter(list(itr)[1:]) if itr_index == 0 else itr

data = csvfile.mapPartitions(lambda x: reader(x)).mapPartitionsWithIndex(remove_header)

law_cat_cd = data.map(lambda x: x[11])

def condition(x):
	if x == '' or x.lower() == 'nan' or x == ' ':
		return ('NaN', 'NULL')
	elif x in ['FELONY', 'MISDEMEANOR', 'VIOLATION']:
		return (x, 'VALID')
	else:
		return (x, 'INVALID')

output = law_cat_cd.map(lambda x:'%s\t%s\t%s\t%s' % (condition(x)[0],'TEXT', 'offense level', condition(x)[1]))
output.saveAsTextFile("column11_data_quality.out")

sc.stop()
            

