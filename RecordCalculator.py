'''
Created on Jan 20, 2016

@version: 0.2
@modification: 01/25/16
@author: jguerra
@return: python script that reads the file and computes 
the number of records (in this file, each line is a record) 
that contain the exact case insensitive phrase "single malt scotch". 
Ignore upper and lower casing, so "Single Malt Scotch", and "SINGLE 
Malt Scotch" all match, whereas "Single's Malty Scootch" does not.
'''

import sys
import csv
import re

usage = "\nusage:   ./RecordCalculator.py [data]\nexample: ./RecordCalculator.py ./iowa-liquor-sample.csv"

# get information from file
def processFile(f_input):
    count = 0
    for row in f_input:
        nrow = [x.lower() for x in row]
        if 'single malt scotch' in nrow:
            count += 1
    return count

if __name__ == '__main__':
    
    filename = None
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    
    if filename:
        with open(filename,'rb') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            data = processFile(csvreader)
        print 'Total number of records containing \'single malt scotch (insensitive)\' : ',
        print data
    else:
        print usage
        exit(0)


