from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import requests
import re
import pandas as pd
import numpy as np

# Extracted images from "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
]

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_news():
    browser = init_browser()

    # Visit visitcostarica.herokuapp.com
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get latest News titles
    all_data = soup.find_all("ul", class_="item_list")

    news_titles = []
    news_para = []
    # Iterate through all data
    for data in all_data:
        titles = data.find_all("div", class_="content_title")
        paras = data.find_all("div", class_="article_teaser_body")

        for title in titles:
            news_titles.append(title.find('a').text)
            # print(title.find('a').text)

        for para in paras:
            news_para.append(para.text)
            # print(para.text)

    # Close the browser after scraping
    browser.quit()

    # Return results
    return news_titles, news_para

def scrape_images():
    browser = init_browser()

    # Visit visitcostarica.herokuapp.com
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    base_url = "https://www.jpl.nasa.gov"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get all Mars featured images
    img_containers = soup.find_all("a", class_="fancybox")
    img_links = []
    img_desc = []
    for img in img_containers:
        img_links.append(img.get('data-fancybox-href'))
        img_desc.append(img.get('data-description'))

    # Close the browser after scraping
    browser.quit()
    idx = np.random.choice(np.arange(len(img_links)), 1, replace = False)
    print(idx)
    # Return results
    return base_url + img_links[idx[0]], img_desc[idx[0]]

def scrape_table_pandas():

    url = "https://space-facts.com/mars/"
    dfs = pd.read_html(url)

    my_table = dfs[0]
    my_table = my_table.rename(columns={0:'description', 1: 'data'}, inplace = False)

    # Return results
    return my_table

def scrape():
    news_titles, news_para = scrape_news()
    featured_img_link, featured_img_desc = scrape_images()
    mars_facts_table = scrape_table_pandas()

    # select random news article from the latest Mars News
    idx = np.random.choice(np.arange(len(news_titles)), 1, replace = False)

    post = {
        'latest_mars_news': [news_titles[idx[0]], news_para[idx[0]]],
        'featured_mars_image': featured_img_link,
        'featured_mars_image_desc' : featured_img_desc,
        'mars_facts_table': mars_facts_table.to_dict('list'),
        'hemisphere_image_urls': hemisphere_image_urls
        }
    return post

