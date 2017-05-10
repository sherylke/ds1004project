# spark-submit NYPD_Motor_Vehicle_Collisions.py /user/YOUR_NETID/NYPD_Motor_Vehicle_Collisions.csv 

# hadoop fs -getmerge NYPD_Motor_Vehicle_Collisions.out NYPD_Motor_Vehicle_Collisions.out 

from __future__ import print_function

import sys
from operator import add
from csv import reader 
from pyspark import SparkContext
import datetime

# COLLISIONS DATA
# DATA SOURCE: 

# make sure the header will not be included in the data 
# source: http://stackoverflow.com/questions/24718697/pyspark-drop-rows
def remove_header(itr_index, itr):
 return iter(list(itr)[1:]) if itr_index == 0 else itr 
 
 
  
if __name__ == "__main__":

 sc = SparkContext()
 
 lines = sc.textFile(sys.argv[1], 1)
 line = lines.mapPartitions(lambda x:reader(x))
 line = line.mapPartitionsWithIndex(remove_header) # remove header 
 line = line.map(lambda x: ((datetime.datetime.strptime(x[0],'%m/%d/%Y').year,datetime.datetime.strptime(x[0],'%m/%d/%Y').month,datetime.datetime.strptime(x[0],'%m/%d/%Y').isocalendar()[1]\
 ,datetime.datetime.strptime(x[0],'%m/%d/%Y').isocalendar()[2]),1))
 
 
 line = line.reduceByKey(lambda x,y: x+y)
 line = line.map(lambda x: '%s\t%s\t%s\t%s\t%s' %(x[0][0],x[0][1],x[0][2],x[0][3],x[1]))
 
 line.saveAsTextFile("NYPD_Motor_Vehicle_Collisions.out") 

 sc.stop()