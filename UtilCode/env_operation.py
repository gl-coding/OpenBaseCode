import datetime
import os

def get_date_str():
    now = datetime.datetime.now()
    strf = now.strftime('%d-%m-%Y %H:%M:%S')
    return strf

def ropen(filename):
    if os.path.exists(filename):
        os.remove(filename)
    return open(filename, "a+")

def init_header(rfile, name="none", brief="none"):
    print >> rfile, "###" * 20
    print >> rfile, "# @author " + name
    print >> rfile, "# @brief  " + brief
    print >> rfile, "# @date   " + get_date_str()
    print >> rfile, "###" * 20
    print >> rfile, "#encoding=utf8"
    print >> rfile, ""

def init_main(rfile):
    print >> rfile, '#coding here'
    print >> rfile, 'def test():'
    print >> rfile, '    print "test"'

    print >> rfile, ''

    print >> rfile, 'if __name__ == "__main__":'
    print >> rfile, '    test()'

def init_code(filepath, name, brief):
    file_pointer = ropen(filepath)
    init_header(file_pointer, name, brief)
    init_main(file_pointer)

if __name__ == "__main__":
    filepath = "test.py"
    name     = "qa_name"
    brief    = "function statement"
    init_code(filepath, name, brief)
