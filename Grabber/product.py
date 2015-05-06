def new_prod():
    return Product()

def new_prod_with_paras(name, desc, link, image_link):
    return Product(name, desc, link, image_link)

class Product:
    
    def __init__(self, name="", desc="", link="", image_link="", ori_price=0.0, curr_price=0.0):
        self.name = name
        self.desc = "empty"
        self.link = link
        self.image_link = image_link
        self.ori_price = ori_price
        self.curr_price = curr_price
        
    def set_name(self, name):
        self.name = name
        
    def set_desc(self, desc):
        self.desc = desc
        
    def set_link(self, link):
        self.link = link
        
    def set_image_link(self, image_link):
        self.image_link = image_link
        
    def set_ori_price(self, ori_price):
        self.ori_price = ori_price
    
    def set_curr_price(self, curr_price):
        self.curr_price= curr_price
        
    def get_name(self):
        return self.name
    
    def get_desc(self):
        return self.desc    
    
    def get_link(self):
        return self.link
    
    def get_image_link(self):
        return self.image_link
    
    def get_ori_price(self):
        return self.ori_price
    
    def get_curr_price(self):
        return self.curr_price