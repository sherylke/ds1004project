from __future__ import print_function

import sys
from operator import add
from csv import reader 
from pyspark import SparkContext
import datetime

# REPORT_DATE
# THIS CODE IS USED TO SUMMARIZE DATA

# make sure the header will not be included in the data 
# source: http://stackoverflow.com/questions/24718697/pyspark-drop-rows
def remove_header(itr_index, itr):
 return iter(list(itr)[1:]) if itr_index == 0 else itr 
 
  
def val_date(report_time): 
# first try to make sure the time is a legal time
 try:
  report = datetime.datetime.strptime(report_time,'%m/%d/%Y')
# second try to make sure the from_datetime is at least earlier than to_datetime
  if report.year<2006 or report.year>2016: 
  # since the report is 2006 ro 2015 for the report time 
   return "INVALID"
  else: 
   return "VALID"
 except:
  if report_time == '':
   return "NULL"
  else:
   return "INVALID" 
   
  
  
if __name__ == "__main__":

 sc = SparkContext()
 
 lines = sc.textFile(sys.argv[1], 1)
 line = lines.mapPartitions(lambda x:reader(x))
 line = line.mapPartitionsWithIndex(remove_header) # remove header 
 line = line.map(lambda x: (val_date(x[5]),1))
 line = line.reduceByKey(lambda x,y: x+y)
 line =line.map(lambda x: '%s\t%s' %(x[0],x[1]))
 line.saveAsTextFile("column5_data_summary.out") 

 sc.stop()
 


