#-*-coding:utf-8-*-

import os, m_utils

file_error = "read file error"
tmp_file = "tmp.txt"
tmp_loc_file = m_utils.get_temp_path() + tmp_file

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
    if not file_loc:
        return False
    elif not os.path.exists(path):
        os.makedirs(path, 0777)
    
    if not os.access(path, os.R_OK):
        return False
    else: 
        return True
    
def write_to_temp(content):
    write_file(tmp_loc_file, content)
    
def read_from_temp():
    return read_file(tmp_loc_file)

def get_tmp_file():
    return tmp_loc_file