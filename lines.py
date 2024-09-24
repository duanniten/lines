import sys

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif len(sys.argv[1])< 3:
    sys.exit('Not a Python file')        
elif sys.argv[1][-3:] != '.py':
    sys.exit('Not a Python file')

try:
    with open(sys.argv[1], 'r') as file:
        line_counter = 0
        for line in file:
            if len(line.strip()) > 0 and line.strip()[0] != '#':
                line_counter += 1
except FileNotFoundError:
    sys.exit('File does not exist')    

print(line_counter)