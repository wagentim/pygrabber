#-*-coding:utf-8-*-

import platform

file_sep = "/"
linux_tmp = "/home/wagentim/temp/"
windows_tmp = "c:/temp/temp/"

def get_path(file_loc):
    if not file_loc:
        return ""
    else:
        index = file_loc.rfind(file_sep)
        if index >= 0:
            return file_loc[0:index]
        else:
            return file_loc
        
def get_file_name(file_loc):
    if not file_loc:
        return ""
    else:
        index = file_loc.rfind(file_sep)
        if index >= 0:
            return file_loc[index + 1:]
        else:
            return file_loc
        
def not_empty(content):
    if not content:
        return False
    else:
        return True
    
def get_temp_path():
    system = platform.system().lower()
    if system == "linux":
        return linux_tmp
    elif system == "windows":
        return windows_tmp
    
def trim_text(text):
    return text.strip()
    
def get_file_name_from_url(url):
    return url.split('/')[-1]