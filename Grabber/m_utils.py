#-*-coding:utf-8-*-

file_sep = "/"

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