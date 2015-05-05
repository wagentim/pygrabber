#-*-coding:utf-8-*-

import m_filehelper as fh
import m_utils

content = "hello world"
file_loc = m_utils.get_temp_path() + "temp.txt"

fh.write_file(file_loc, content)
print(fh.read_file(file_loc))