import sqlite3

handler_list = {}

def get_handler(name):
    if not name:
        return None
    else:
        if name not in handler_list.keys():
            handler = DBHandler(name)
            handler_list[name] = handler
            return handler
        else:
            return handler_list[name]

def release_handlers():
    for name in handler_list.keys():
        handler_list[name].close()

class DBHandler:
    
    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.c = self.conn.cursor()
    
    def execute(self, command):
        self.c.execute(command)
        self.conn.commit()
            
    def close(self):
        self.c.close()
        self.conn.close()
    