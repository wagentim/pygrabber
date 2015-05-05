#-*-coding:utf-8-*-

import m_nethelper as nh
import m_filehelper as fh
import m_utils as ut
from bs4 import BeautifulSoup as bs

identify = "Baby Market: "
addr = "http://www.baby-markt.de/"
TAGE_ANGEBOT = "Tagesangebot!"
# get page content
content = nh.get_page(addr)

#if ut.not_empty(content):
#    fh.write_to_temp(content)
#    print("write content to the temp file: " + fh.get_tmp_file())
#else:
#    print(identify + "cannot get main page content")
    
content = fh.read_from_temp()
soup = bs(content)
a_link = soup.findAll("a", title = TAGE_ANGEBOT)
for link in a_link:
    print(link)