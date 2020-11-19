import pandas as pd

from requests import get
from bs4 import BeautifulSoup
from time import sleep


def make_soup(url=''):
    '''
    This helper function takes in a url and requests and parses HTML
    returning a soup object.
    '''
    headers = {'User-Agent': 'Codeup Data Science'} 
    response = get(url, headers=headers)    
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def get_url_pages():
    '''
    This function creates a list of url pages 
    with specified languages and topics
    '''
    urls = []
    languages = ['JavaScript', 'Python', 'Java', 'C%2B%2B']
    topics = ['sports', 'data+engineering', 'artificial+intelligence', 'space+exploration', 'biology']
    for language in languages:
        for topic in topics:
            urls.append(f"https://github.com/search?l={language}&q={topic}&type=Repositories")
    return urls


def get_url_links(urls=[]):
    '''
    This function creates a list of 10 urls from a single page
    '''
    extensions = []

    for url in urls:
        soup = make_soup(url)
        sleep(3)
        extension = soup.find_all("a", {"class":"v-align-middle"}, {"data-hydro-click":"url"})
        for count in range(len(extension)):
            extensions.append("http://github.com/" + extension[count].get_text())
    return extensions


def scrape_respositories(repository_urls=[]):
    pass