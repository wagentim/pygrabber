#-*-coding:utf-8-*-

import httplib2
import m_utils
import urllib2

def get_page(url):
    
    if not m_utils.not_empty(url):
        return ""
    else:
        h = httplib2.Http(".cache")
        (resp, content) = h.request(url, "GET")
        return content
    
def download(url, file_loc):
    file_name = m_utils.get_file_name_from_url(url)
    u = urllib2.urlopen(url)
    # here we need to 
    f = open(file_loc+file_name, 'w+')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
    
        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,

    f.close()