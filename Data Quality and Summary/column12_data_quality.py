#!/usr/bin/env python

import sys
from csv import reader
from pyspark import SparkContext

sc = SparkContext()

csvfile = sc.textFile(sys.argv[1], 1)

def remove_header(itr_index, itr):
        return iter(list(itr)[1:]) if itr_index == 0 else itr

data = csvfile.mapPartitions(lambda x: reader(x)).mapPartitionsWithIndex(remove_header)

pd_cd = data.map(lambda x: x[12])

def condition(x):
        if x == '' or x.lower() == 'nan' or x == ' ':
                return ('NaN', 'NULL')
        else:
		return (x, 'VALID')

output = pd_cd.map(lambda x:'%s\t%s\t%s\t%s' % (condition(x)[0],'TEXT', 'jurisdiction description', condition(x)[1]))
output.saveAsTextFile("column12_data_quality.out")

sc.stop()
