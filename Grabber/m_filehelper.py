#-*-coding:utf-8-*-

import os, m_utils

file_error = "read file error"
tmp_loc = "c:/temp/parser.txt"

def write_file(file_loc, content):
    if check_file(file_loc):
        f = open(file_loc, "w+")
        f.write(content)
        f.close()
    else:
        print(file_error)

def read_file(file_loc):
    if check_file(file_loc):
        f = open(file_loc, "r")
        content = f.read()
        f.close()
        return content
    else:
        print(file_error)

def check_file(file_loc):
    
    path = m_utils.get_path(file_loc)
    print(path)
    if not file_loc:
        return False
    elif not os.path.exists(path):
        os.makedirs(path, 0777)
    
    if not os.access(path, os.R_OK):
        return False
    else: 
        return True
    
def write_to_temp(content):
    write_file(tmp_loc, content)
    
def read_from_temp():
    return read_file(tmp_loc)