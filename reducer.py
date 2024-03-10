import sys

def _format_and_split(line,separator='\t'):
    return line.strip().split(separator)

def _emit(elements, separator='\t'):
    elements_as_string = map(str, elements)
    output_string = separator.join(elements_as_string)
    print(output_string)

def _city_changed(city_of_previous_line, city_of_current_line):
    return (city_of_previous_line) and (city_of_previous_line != city_of_current_line)

def reducer():
    total_sales_of_city = 0
    city_of_previous_line = None
    
    for line in sys.stdin:
        line_elements = _format_and_split(line)
        
        if len(line_elements) != 2:
            continue
        
        city_of_current_line, city_of_current_sale = line_elements
        
        if _city_changed(city_of_previous_line, city_of_current_line):
            _emit([city_of_previous_line,total_sales_of_city])
            
            total_sale_of_city=0
            
        city_of_previous_line = city_of_current_line
        total_sales_of_city += float(city_of_current_sale)
        
        if not city_of_current_line :
            _emit([city_of_previous_line,total_sales_of_city])

if __name__ == '__main__':
     reducer()
