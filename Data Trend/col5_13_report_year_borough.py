from __future__ import print_function

import sys
from operator import add
from csv import reader 
from pyspark import SparkContext
import datetime

# REPORT_DATE BY YEAR & BY KY_CD


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


def condition(x):
 if x == '' or x.lower() == 'nan' or x == ' ':
  return 'NULL'
 elif x in ['BRONX', 'QUEENS', 'MANHATTAN', 'BROOKLYN', 'STATEN ISLAND']:
  return  'VALID'
 else:
  return  'INVALID'
  
if __name__ == "__main__":

 sc = SparkContext()
 
 lines = sc.textFile(sys.argv[1], 1)
 line = lines.mapPartitions(lambda x:reader(x))
 line = line.mapPartitionsWithIndex(remove_header) # remove header 
 line = line.map(lambda x: [x[5],x[13],val_date(x[5])])
 line = line.filter(lambda x:x[2]== "VALID") # only look for valid date 
 line = line.map(lambda x: [x[0],x[1],condition(x[1])])
 line = line.filter(lambda x: x[2] =="VALID")
 line = line.map(lambda x: ((datetime.datetime.strptime(x[0],'%m/%d/%Y').year,x[1]),1))
 line = line.reduceByKey(lambda x,y: x+y)
 line = line.map(lambda x: '%s\t%s\t%s' %(x[0][0],x[0][1],x[1]))
 
 line.saveAsTextFile("col5_13_report_year_borough.out") 

 sc.stop()


