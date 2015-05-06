#-*-coding:utf-8-*-

import m_nethelper as nh
import m_utils as ut
from bs4 import BeautifulSoup as bs
import product


class BabyMarket:
    
    IDENTITY = "Baby Market: "
    DOMAIN = "http://www.baby-markt.de/"
    only_main_angebot = False
    parser_level = 1
    products = []
    main_category_links = []
    sub_category_links = []
    
    def set_only_main_angobot(self, value):
        self.only_main_angebot = value
    
    def is_only_main_angebot(self):
        return self.only_main_angebot
    
    def process(self):
        if self.is_only_main_angebot():
            self.do_grab_main_angebot()
        else:
            self.do_grab_all_products()
            
    def do_grab_all_products(self):
        #self.content = nh.get_page(self.DOMAIN)
        #if self.content and len(self.content) > 0:
            #fh.write_to_temp(self.content)
        self.parser_links()
        print("--- parser links finished")
        print("--- Main Categories: " + str(len(self.main_category_links)))
        print("--- Main Categories: " + str(len(self.sub_category_links)))
        
        if self.sub_category_links and len(self.sub_category_links) > 0:
            for link in self.sub_category_links:
                self.parser_prods(link)
        else:
            print("--- Cannot parser site: " + self.DOMAIN)
        return
            
    def do_grab_main_angebot(self):
        return
    
    def get_domain(self):
        return self.DOMAIN
    
    def parser_prods(self, url):
        print("--- parser products in the link: " + url)
        inhalt = nh.get_page(url)
        soup = bs(inhalt)
        # get product
        prods = soup.select(".list-product")
        if prods and len(prods) > 0:
            for prod in prods:
                prodt = product.new_prod()
 
                #set liink
                image_block = prod.select(".image")
                prodt.set_link(self.DOMAIN[0:len(self.DOMAIN) - 1] + image_block[0].a.get("href"))
                
                #set name
                prodt.set_name(prod.select(".title")[0].text)
                
                #set current price
                prodt.set_curr_price(prod.select(".price")[0].text)
                
                #set original price
                del_tag = prod.select("del")
                if del_tag and len(del_tag) > 0:
                    prodt.set_ori_price(del_tag[0].text)
                else:
                    prodt.set_ori_price(prodt.get_curr_price())
                #set description
                #set image link
                prodt.set_image_link("http:" + prod.select("img")[0].get("src"))
                self.products.append(prodt)
                
                print("Product: " + prodt.get_name() + "\nOriginal Price: " + prodt.get_curr_price() + "\nOriginal Price: " + prodt.get_ori_price() + "\nLink: " + prodt.get_link() + "\nImage Link: " + prodt.get_image_link())
                print("------------------------------")

    
    def get_main_content(self):   
        
        if not self.soup:
            return None
        else:
            locs = [];
            items = self.soup.findAll("div", {"class" : "slide-content"})
            for item in items:
                links = item.findAll("a")
                cached_loc = ""
                cached_text = ""
                for link in links:
                    text = ut.trim_text(link.text)
                    if len(text) <= 0:
                        text = ""
                    loc = self.DOMAIN[0:len(self.DOMAIN)-1] + link.get("href")
                    if cached_loc == loc:
                        cached_text += text
                    else:
                        cached_loc = loc
                        if cached_loc != "":
                            cached_loc = loc
                            print(cached_text + "\n" +loc + "\n")
            return locs
                    
    def parser_links(self):
        
        print("--- parser links start...")
        
        curr_content = nh.get_page(self.DOMAIN)
        if ut.not_empty(curr_content):
            soup = bs(curr_content)
            categories = soup.select(".dropdown-menu-subcategories")
            if categories and len(categories) > 0:
                
                for cate in categories:
                    
                    active_link = cate.select(".active-main-category")[0].a.get("href")
                    
                    if active_link and len(active_link) > 0:
                        
                        self.main_category_links.append(self.DOMAIN[0:len(self.DOMAIN)-1] + active_link)
                    
                        sub_cate_links = cate.findAll("a")
                        
                        if sub_cate_links and len(sub_cate_links) > 0:
                            
                            for sub_link in sub_cate_links:
                                l = sub_link.get("href")
                                
                                if "#" not in l and "http" not in l and "https" not in l and active_link != l:
                                    self.sub_category_links.append(self.DOMAIN[0:len(self.DOMAIN)-1] + l)
                                    

    def get_main_category_links(self):
        return self.main_category_links
    
    def get_all_parser_page_links(self):
        return self.sub_category_links
