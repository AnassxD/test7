#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment

# We want elements 2 (store name) and 4 (cost)
# We want to write them out to standard output, separated by a tab

import sys

def _format_and_split(line, separator='\t'):
    return line.strip().split(separator)

def _emit(elements, separator='\t'):
    elements_as_string = map(str, elements)
    output_string = separator.join(elements_as_string)
    print(output_string)

def mapper():
    for line in sys.stdin:
        line_elements = _format_and_split(line)
        
        if len(line_elements) != 6:
            continue
        
        date, time, store, item, cost, payment_method = line_elements
        _emit([store, cost])

if __name__== '__main__':
    mapper()
