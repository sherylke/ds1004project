# spark-submit col5_summary_time.py /user/YOUR_NETID/NYPD_Complaint_Data_Historic.csv
# hadoop fs -getmerge col5_summary_time.out col5_summary_time.out 

from __future__ import print_function

import sys
from operator import add
from csv import reader 
from pyspark import SparkContext
import datetime

# REPORT_DATE 

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
 line = line.map(lambda x: [x[5],val_date(x[5])])
 line = line.filter(lambda x:x[1]== "VALID")

 line = line.map(lambda x: ((datetime.datetime.strptime(x[0],'%m/%d/%Y').year,datetime.datetime.strptime(x[0],'%m/%d/%Y').month,datetime.datetime.strptime(x[0],'%m/%d/%Y').isocalendar()[1]\
 ,datetime.datetime.strptime(x[0],'%m/%d/%Y').isocalendar()[2]),1))
 
 
 line = line.reduceByKey(lambda x,y: x+y)
 line = line.map(lambda x: '%s\t%s\t%s\t%s\t%s' %(x[0][0],x[0][1],x[0][2],x[0][3],x[1]))
 
 line.saveAsTextFile("col5_summary_time.out") 

 sc.stop()