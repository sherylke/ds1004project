import sys
from csv import reader
from pyspark import SparkContext

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
            return (x23, p)

if __name__ == "__main__":
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x: reader(x)).mapPartitionsWithIndex(remove_header)
    result = lines.map(lambda x: (x[21],x[22],x[23]))\
             .map(lambda x:'%s\t%s\t%s\t%s' % (condition(x[0],x[1],x[2])[0],'DECIMAL', 'Location for Global Coordinate System', condition(x[0],x[1],x[2])[1]))
    result.saveAsTextFile("column23_data_quality.out")

    sc.stop()
