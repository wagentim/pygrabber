#-*-coding:utf-8-*-

import h_babymarket

baby_market = h_babymarket.BabyMarket()
baby_market.set_only_main_angobot(False)
baby_market.process()
#baby_market.parser_prods("http://www.baby-markt.de/markenshop-chicco/")
#baby_market.get_all_prods()