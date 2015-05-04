#-*-coding:utf-8-*-

import httplib2
import m_utils

def get_page(url):
    
    if not m_utils.not_empty(url):
        return ""
    else:
        h = httplib2.Http(".cache")
        (resp, content) = h.request(url, "GET")
        return content