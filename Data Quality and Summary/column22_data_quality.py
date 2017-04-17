import sys
from csv import reader
from pyspark import SparkContext

def remove_header(itr_index, itr):
        return iter(list(itr)[1:]) if itr_index == 0 else itr

def condition(x):
        if x == '':
                return ('NaN', 'NULL')
        else:
            try:
                i = float(x)
                if (i>-74.2560) & (i<-73.7):
                    p = 'VALID'
                else:
                    p = 'INVALID'
                return (x, p)
            except:
                return (x, 'INVALID')

if __name__ == "__main__":
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x: reader(x)).mapPartitionsWithIndex(remove_header)
    result = lines.map(lambda x: x[22])\
             .map(lambda x:'%s\t%s\t%s\t%s' % (condition(x)[0],'DECIMAL', 'Longitude for Global Coordinate System', condition(x)[1]))
    result.saveAsTextFile("column22_data_quality.out")

    sc.stop()
