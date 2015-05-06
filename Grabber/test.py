#-*-coding:utf-8-*-

import h_babymarket
import m_dbhelper
import sql

#baby_market = h_babymarket.BabyMarket()
#baby_market.set_only_main_angobot(False)
#baby_market.process()
#baby_market.parser_prods("http://www.baby-markt.de/markenshop-chicco/")
#baby_market.get_all_prods()
handler = m_dbhelper.get_handler("production.db")
#handler.execute(sql.create_product_table())
baby_market = h_babymarket.BabyMarket()
baby_market.set_only_main_angobot(True)
baby_market.process()
for prod in baby_market.get_parsered_products():
    handler.execute(sql.inser_product(prod))
m_dbhelper.release_handlers()
