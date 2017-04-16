#!/usr/bin/env python

import sys
from csv import reader
from pyspark import SparkContext

sc = SparkContext()

csvfile = sc.textFile(sys.argv[1], 1)

def remove_header(itr_index, itr):
        return iter(list(itr)[1:]) if itr_index == 0 else itr

data = csvfile.mapPartitions(lambda x: reader(x)).mapPartitionsWithIndex(remove_header)

code = data.map(lambda x: x[19])

def condition(x):
	try:
        	if x == '' or x.lower() == 'nan' or x == ' ':
                	return ('NaN', 'NULL')
        	elif 909900 <= int(x) <= 1067600: 
		# http://answers.google.com/answers/threadview?id=545900
                	return (x, 'VALID')
        	else:
             		return (x, 'INVALID')
	except ValueError:
		return (x, 'INVALID')

output = code.map(lambda x:'%s\t%s\t%s\t%s' % (condition(x)[0],'INT', 'x coordinate number', condition(x)[1]))
output.saveAsTextFile("x_coord_cd.out")

sc.stop()