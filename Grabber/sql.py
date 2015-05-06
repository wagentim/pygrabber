
def create_product_table():
    content = '''CREATE TABLE PRODUCT
       (NAME            TEXT    NOT NULL,
       DESC            TEXT,
       ORIG_PRICE      INT     NOT NULL,
       CURR_PRICE      INT     NOT NULL,
       LINK            TEXT,
       IMAGE_LINK      TEXT);'''
    return content

def inser_product(prod):
    print(prod.get_ori_price())
    content = "INSERT INTO PRODUCT VALUES ('" + prod.get_name() + "','" + prod.get_desc() + "','" + prod.get_ori_price() + "','" + prod.get_curr_price() + "','" + prod.get_link() + "','" + prod.get_image_link() + "')"
    print(content)
    return content
