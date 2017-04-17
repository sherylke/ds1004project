#!/usr/bin/env python

import sys
from csv import reader
from pyspark import SparkContext

sc = SparkContext()

csvfile = sc.textFile(sys.argv[1], 1)

def remove_header(itr_index, itr):
	return iter(list(itr)[1:]) if itr_index == 0 else itr

data = csvfile.mapPartitions(lambda x: reader(x)).mapPartitionsWithIndex(remove_header)

pd_cd = data.map(lambda x: x[8])

def condition(x):
        try:
            	if x == '' or x.lower() == 'nan' or x == ' ':
                        return ('NaN', 'NULL')
                elif str(int(x)) == x and len(str(int(x))) == 3:
                        return (x, 'VALID')
                else:
                     	return (x, 'INVALID')
        except ValueError:
                return (x, 'INVALID')

output = pd_cd.map(lambda x:'%s\t%s\t%s\t%s' % (condition(x)[0],'INT', 'internal classification code', condition(x)[1]))
output.saveAsTextFile("column8_data_quality.out")

sc.stop()

