import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.headless = True

class TrendingTickers:
    def __init__(self):
        self.bot = webdriver.Firefox(options=options)
        self.ttickers = []

    def start(self):
        bot = self.bot
        bot.get("https://stockbeep.com/trending-stocks")

    def getData(self):
        data = []
        table = self.bot.find_elements_by_class_name("column-sscode")
        for row in table:
            self.ttickers.append(row.text)
        self.ttickers = self.ttickers[1:6]
        for t in self.ttickers:
            data.append(t)
        return data 



if __name__ == "__main__":
    bot = TrendingTickers()
    bot.start()
    bot.getData()