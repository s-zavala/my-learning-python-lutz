#!python
"""
Count number of lines or characters in a file.
"""
import sys


def count_lines(file_handle):
    line_count =  len(file_handle.readlines())
    print(f'Number of lines -- {line_count}')
        

def count_chars(file_handle):
    char_count = len(file_handle.read())
    print(f'Number of characters -- {char_count}')

def test(name):
    with open(name, 'r') as file_handle:    
        count_lines(file_handle)
        file_handle.seek(0)
        count_chars(file_handle)

if __name__ == "__main__":
    if len(sys.argv) != 1:
        name = sys.argv[1]
        test(name)
    else:
        print('Need a file name.')