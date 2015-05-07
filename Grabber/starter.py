# start grabber each day and same the data to DB
import h_babymarket

bm = h_babymarket.BabyMarket()
bm.set_only_main_angobot(True)
bm.process()