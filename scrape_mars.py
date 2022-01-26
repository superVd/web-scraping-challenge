# Import Splinter, BeautifulSoup, and Pandas
import pandas as pd
from bs4 import BeautifulSoup as soup 
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    return_dict  = {}

    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    #----------------Nasa Mars News-----------------------------------------
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    
    #---------------store in soup
    html = browser.html
    red_planet_soup =soup(html,"html.parser") 

    
    #read webpage html
    redplanet_news = red_planet_soup.select_one("div.list_text")
    news_title  = redplanet_news.find("div", class_= "content_title").get_text()
    return_dict["key_newstitle"] = news_title

    newspara = redplanet_news.find("div", class_= "article_teaser_body").get_text()
    return_dict["key_newspara"] = newspara

    news_date = redplanet_news.find("div", class_= "list_date").get_text()
    return_dict["key_newsdate"] = news_date
