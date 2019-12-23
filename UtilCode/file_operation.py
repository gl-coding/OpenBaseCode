#encoding=utf8
import os

#dir operation, line first layer
def dir_scan(dir_path):
    for d in os.listdir(dir_path):
        print d

#遍历filepath下所有文件，包括子目录
def dir_scan_all(dir_path):
    files = os.listdir(dir_path)
    for fi in files:
        full_path = os.path.join(dir_path, fi)
        if os.path.isdir(full_path):
            dir_scan_all(full_path)
        else:
            print full_path

#file operation
def file_line_read(filepath):
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            print line

#for >> log
def ropen(filename):
    if os.path.exists(filename):
        os.remove(filename)
    return open(filename, "a+")
