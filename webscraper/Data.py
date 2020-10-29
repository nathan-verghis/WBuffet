import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

class TrendingTickers:
    def __init__(self):
        self.bot = webdriver.Firefox()
        self.ttickers = []

    def start(self):
        bot = self.bot
        bot.get("https://stockbeep.com/trending-stocks")

    def getData(self):
        '''page = self.bot.find_element_by_id("DataTables_Table_0_wrapper")
        table = page.table
        value = []
        for row in table:
            value.append(row.find_element_by_class_name("column-sscode"))
        for row in value:
            row = row.text
            print(row)'''
        table = self.bot.find_elements_by_class_name("column-sscode")
        for row in table:
            self.ttickers.append(row.text)
        self.ttickers = self.ttickers[1:11]
        for t in self.ttickers:
            print(t) 



bot = TrendingTickers()
bot.start()
bot.getData()