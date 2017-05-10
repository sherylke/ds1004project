# spark-submit col5_compared_to_zipcode.py /user/YOUR_NETID/NYPD_Complaint_Data_Historic.csv /user/YOUR_NETID/zipcode.csv 
# hadoop fs -getmerge col5_compared_to_zipcode.out col5_compared_to_zipcode.out 

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

def condition21(x):
 if x == '':
  return 'NULL'
 else:
  try:
   i = float(x)
   if (i>40.4980) & (i<40.9128):
    p = 'VALID'
   else:
    p = 'INVALID'
   return p
  except:
   return 'INVALID'

def condition22(x):
 if x == '':
  return 'NULL'
 else:
  try:
   i = float(x)
   if (i>-74.2560) & (i<-73.7):
    p = 'VALID'
   else:
    p = 'INVALID'
   return p
  except:
   return 'INVALID'

def condition(x21, x22, x23):
 if x23 == '':
  return ('NaN', 'NULL')
 else:
  if (condition21(x21) == 'VALID') & (condition22(x22) == 'VALID') :
   p = 'VALID'
  else:
   p = 'INVALID'
  return  p
  
  
   
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
 zip = sc.textFile(sys.argv[2], 1)
 lines = lines.mapPartitions(lambda x: reader(x)).mapPartitionsWithIndex(remove_header)
 zip = zip.mapPartitions(lambda x: reader(x)).mapPartitionsWithIndex(remove_header)
 result = lines.map(lambda x: (x[5],x[21],x[22],x[23]))
 
 result = result.filter(lambda x: val_date(x[0]) =="VALID")
 result = result.filter(lambda x: condition(x[1],x[2],x[3]) =="VALID") 
 
 result = result.map(lambda x: (x[3],x[0])) 
  
 zip = zip.map(lambda x: (x[1],x[2]))
 
 output = result.leftOuterJoin(zip) 
 output = output.map(lambda x: ((x[1][1],datetime.datetime.strptime(x[1][0],'%m/%d/%Y').year,datetime.datetime.strptime(x[1][0],'%m/%d/%Y').month,datetime.datetime.strptime(x[1][0],'%m/%d/%Y').isocalendar()[1]\
 ,datetime.datetime.strptime(x[1][0],'%m/%d/%Y').isocalendar()[2]),1)) 
 
 output = output.reduceByKey(lambda x,y: x+y)
 line = output.map(lambda x: '%s\t%s\t%s\t%s\t%s\t%s' %(x[0][0],x[0][1],x[0][2],x[0][3],x[0][4],x[1]))
 
 line.saveAsTextFile("col5_compared_to_zipcode.out") 
 
 sc.stop()
 