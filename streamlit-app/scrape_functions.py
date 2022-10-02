from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def get_title(soup):
    temp_title = ''
    for a in soup.findAll('div', attrs={'class':'content-thin'}):
        for b in a.findAll('h1'):
                temp_title = (b.text.replace('\n', ''))
    return temp_title

def get_body(soup):
    for a in soup.findAll('article'):
        return a.text.replace('\n', '')
    
def get_tags(soup):
    tags = []
    tag_holder = []
    for a in soup.findAll('section'):
        for b in a.findAll('p'):
            for c in b.findAll('a', href=True, attrs={'class':'btn-grey-dark btn-xxs btn-rounded space-right-xs-sm'}):
                tag_holder.append(c.text)
    tags.append(','.join(tag_holder))
    return tags[0]

def scrape_content(soup, url):
    title = []
    body = []
    tags = []
    urls = []
    title.append(get_title(soup))
    body.append(get_body(soup))
    urls.append(url)
    tags.append('')
    ## tags.append(get_tags(soup))
    return pd.DataFrame({'Article title':title,'Body':body, 'URL':url, 'Tags':tags})

def scrape_URL(url, driver):
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")
    return scrape_content(soup, url)