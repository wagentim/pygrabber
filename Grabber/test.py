#-*-coding:utf-8-*-

import m_filehelper as fh

content = "hello world"
file_loc = "c:/temp/temp/temp.txt"

fh.write_file(file_loc, content)
print(fh.read_file(file_loc))