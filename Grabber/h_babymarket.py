#-*-coding:utf-8-*-

import m_nethelper as nh
import m_filehelper as fh
import m_utils as ut

identify = "Baby Market: "
addr = "http://www.baby-markt.de/"

# get page content
content = nh.get_page(addr)

if ut.not_empty(content):
    fh.write_to_temp(content)
    print("write content to the temp file")
else:
    print(identify + "cannot get main page content")
    

