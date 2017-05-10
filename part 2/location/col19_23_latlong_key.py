# spark-submit col19_23_latlong_key.py /user/YOUR_NETID/NYPD_Complaint_Data_Historic.csv
# hadoop fs -getmerge col19_23_latlong_key.out col19_23_latlong_key.out


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

if __name__ == "__main__":
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x: reader(x)).mapPartitionsWithIndex(remove_header)
    result = lines.map(lambda x: (x[21],x[22],x[23]))
    result = result.map(lambda x: (x[0],x[1],condition(x[0],x[1],x[2])))
    result = result.filter(lambda x: x[2] =="VALID") 
    result = result.map(lambda x:((x[0],x[1]),1)).reduceByKey(lambda x,y: x+y)
    result = result.map(lambda x:'%s\t%s\t%s' %(x[0][0],x[0][1],x[1]))
    result.saveAsTextFile("col19_23_latlong_key.out") 
   
 
 
    sc.stop()
 
