#encoding=utf8
import os

#dir operation
def dir_scan(dir_path):
    for d in os.listdir(dir_path):
        print d

#file operation
def file_line_read(filepath):
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            print line

def ropen(filename):
    if os.path.exists(filename):
        os.remove(filename)
    return open(filename, "a+")
