#!/usr/bin/env python

import sys
from csv import reader
from pyspark import SparkContext

sc = SparkContext()

csvfile = sc.textFile(sys.argv[1], 1)

def remove_header(itr_index, itr):
        return iter(list(itr)[1:]) if itr_index == 0 else itr

data = csvfile.mapPartitions(lambda x: reader(x)).mapPartitionsWithIndex(remove_header)

code = data.map(lambda x: x[18])

with open('hadevelopt.txt','r') as f:
	names = f.readlines()
# http://www1.nyc.gov/site/nycha/about/developments.page

for i in range(len(names)):
	names[i] = names[i].split('\n')[0]
	names[i] = names[i].upper()

def condition(x):
        if x == '' or x.lower() == 'nan' or x == ' ':
                return (x, 'NULL')
        elif x in names:
                return (x, 'VALID')
        else:
             	return (x, 'INVALID')

line = code.map(lambda x: condition(x))

output = line.filter(lambda x: x[-1]=='INVALID').map(lambda x: (x[0],1)).reduceByKey(lambda x,y: x+y).map(lambda x: '%s\t%s' % (x[0],x[1]))
output.saveAsTextFile("column18_data_quality_issue.out")

sc.stop()
