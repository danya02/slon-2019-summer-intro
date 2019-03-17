#!/usr/bin/python3
import sys
from math import floor, ceil

maxv=float('inf')
minv=float('-inf')

values = []
for index,value in enumerate(sys.stdin):
    try:
        value = float(value)
        maxv=max(maxv,value)
        minv=min(minv,value)
        values.append(value)
    except ValueError:
        print(f'Line {index+1} does not contain a valid float. If there is no further input, please enter a EOT character (ASCII 0b00000100) into your terminal.')

class FloatRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __contains__(self, value):
        return value>=self.start and value<self.end

ranges = [FloatRange(n,n+1) for n in range(floor(minv), ceil(maxv)+1)]
columns = [0 for i in ranges]

for i in values:
    for index,range_obj in enumerate(ranges):
        if i in range_obj:
            columns[index]+=1
columns = [ceil(i/20) for i in columns]

for line in range(max(columns),0,-1):
    print(''.join(['*' if line<column else ' ' for column in columns]))
