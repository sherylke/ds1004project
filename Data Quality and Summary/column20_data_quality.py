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
                i = int(x)
                if (i>120800) & (i<271900):
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
    result = lines.map(lambda x: x[20])\
             .map(lambda x:'%s\t%s\t%s\t%s' % (condition(x)[0],'INTEGER', 'Y-coordinate for New York State Plane Coordinate System', condition(x)[1]))
    result.saveAsTextFile("column20_data_quality.out")

    sc.stop()
