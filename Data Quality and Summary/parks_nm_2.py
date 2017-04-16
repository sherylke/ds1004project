#!/usr/bin/env python

import sys
from csv import reader
from pyspark import SparkContext

sc = SparkContext()

csvfile = sc.textFile(sys.argv[1], 1)

with open('parks_nm.txt','r') as f:
	names = f.readlines()
for i in range(len(names)):
	names[i] = names[i].split('\n')[0]
	names[i] = names[i].upper()

def remove_header(itr_index, itr):
        return iter(list(itr)[1:]) if itr_index == 0 else itr

data = csvfile.mapPartitions(lambda x: reader(x)).mapPartitionsWithIndex(remove_header)

code = data.map(lambda x: x[17])

def condition(x):
        if x == '' or x.lower() == 'nan' or x == ' ':
                return ('NaN', 'NULL')
        elif x in names:
		return (x, 'VALID')
	else:
             	return (x, 'INVALID')

output = code.map(lambda x:'%s\t%s\t%s\t%s' % (condition(x)[0],'TEXT', 'park names', condition(x)[1]))
output.saveAsTextFile("parks_nm_2.out")

sc.stop()
