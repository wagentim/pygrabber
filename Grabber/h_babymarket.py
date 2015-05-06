#-*-coding:utf-8-*-

import m_nethelper as nh
import m_utils as ut
from bs4 import BeautifulSoup as bs
import product
import m_filehelper as fh


class BabyMarket:
    
    IDENTITY = "Baby Market: "
    DOMAIN = "http://www.baby-markt.de/"
    only_main_angebot = True
    parser_level = 1
    products = []
    main_category_links = []
    sub_category_links = []
    soup = None
    
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
        self.products[:] = []
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
                self.print_prods()
    
    def print_prods(self):
        if len(self.products) > 0:
            for prodt in self.products:
                if prodt.get_curr_price() != prodt.get_ori_price():
                    percent = ut.get_price_percent(prodt)
                    if percent < 45:
                        print("Product: " + prodt.get_name() + "\nCurrent Price: " + prodt.get_curr_price() + "\nOriginal Price: " + prodt.get_ori_price() + "\nLink: " + prodt.get_link() + "\nImage Link: " + prodt.get_image_link())
                        print("Percent: " + str(percent))
                        print("------------------------------")
    
    def do_grab_main_angebot(self):   
        self.products[:] = []
        self.parser_links()
        print("--- parser content start...")
        #get angebot in main page
        slide_content = self.soup.select(".slide-content")
        if slide_content and len(slide_content) > 0:
            links = []
            for content in slide_content:
                link = content.select("a")
                if len(link) > 0:
                    for l in link:
                        links.append(l)
                else:
                    links.append(link)
            tmp = []
            for li in links:
                tit = li.select(".title")
                if tit and len(tit) > 0:
                    prod = product.new_prod()
                    prod.set_name(tit[0].text)
                    prod.set_curr_price(li.select(".price")[0].text)
                    prod.set_ori_price(li.select(".old-price")[0].text)
                    prod.set_link(li.get("href"))
                    prod.set_image_link("http" + li.select(".image")[0].get("data-original"))
                    self.products.append(prod)
                else:
                    u_loc = self.DOMAIN[0:len(self.DOMAIN)-1] + li.get("href")
                    tmp.append(u_loc)
            if len(tmp) > 0:
                for page in tmp:
                    self.parser_prods(page)
           
        
    def parser_links(self):
        print("--- parser links start...")
        curr_content = nh.get_page(self.DOMAIN)
        #fh.write_to_temp(curr_content)
        #curr_content = fh.read_from_temp()
        if ut.not_empty(curr_content):
            self.soup = bs(curr_content)
            categories = self.soup.select(".dropdown-menu-subcategories")
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
    
    def get_parsered_products(self):
        return self.products
