#-*-coding:utf-8-*-

import m_nethelper as nh
import m_utils as ut
import m_filehelper as fh
from bs4 import BeautifulSoup as bs
import m_utils

class BabyMarket:
    
    IDENTITY = "Baby Market: "
    DOMAIN = "http://www.baby-markt.de/"
    ADV = "slide-content"
    shouldReload = False
    ignore_text = ["Merkzettel", "Geschenketisch", "Kontakt", "Mein Konto", "Newsletter", "Geschenkgutscheine", "Filialen", "Kategorien",
                   "Über uns", "Datenschutz", "Widerrufsrecht", "AGB/Verbraucherinformationen", "Zahlung und Versand", "Impressum", "Karriere",
                   "Filialen", "Kontakt", "Newsletter", "Partnerprogramme", "jetzt sammeln", "Startseite", "Kontakt", "AGB/Verbraucherinformationen",
                   "Datenschutz", "Batterie-Rücknahme", "schließen"]
    
    loc_list = []
    
    #def __init__(self):
        
        #self.content = nh.get_page("http://www.baby-markt.de/autositze/")
        #fh.write_to_temp(self.content)
        #if ut.not_empty(self.content):
        #    self.content = fh.read_from_temp()
        #    self.soup = bs(self.content)
        #else:
        #    print(self.IDENTITY + "cannot get main page content")
        #    return
          
    def get_prods(self):
        self.content = fh.read_from_temp()
        soup = bs(self.content)
        links = soup.findAll("a")
        for link in links:
            text = ut.trim_text(link.text)
            if len(text) <= 0:
                text = ""
            href = link.get("href")
            if href:
                loc = self.DOMAIN[0:len(self.DOMAIN)-1] + href
                print(text + "\n" +loc + "\n")
    
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
                    
    def get_all_prods(self):
        
        self.loc_list.append(self.DOMAIN)
        page_level = 0;
        
        while len(self.loc_list) > 0 and page_level < 1:
            
            curr_loc = self.loc_list.pop()
            
            if ut.not_empty(curr_loc):
                curr_content = nh.get_page(curr_loc)
                
                if ut.not_empty(curr_loc):
                    
                    if page_level == 0:
                        items = bs(curr_content).findAll("a")
                    
                    for item in items:
                            link = item.get("href")
                            if link and "http" not in link and "https" not in link and link != "#" and link != "/":
                                n_link = self.DOMAIN[0:len(self.DOMAIN)-1] + link
                                if n_link not in self.loc_list:
                                    self.loc_list.append(n_link)
                                    
            page_level += 1
                    
        for loc in self.loc_list:
            print(loc)   
         
        
        
                    

