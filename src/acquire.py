import pandas as pd

from requests import get
from bs4 import BeautifulSoup
from time import sleep


def make_soup(url=''):
    '''
    This helper function takes in a url and requests and parses HTML
    returning a soup object.
    '''
    headers = {'User-Agent': 'NLP3'} 
    response = get(url, headers=headers)
    sleep(3)
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
        extension = soup.find_all("a", {"class":"v-align-middle"}, {"data-hydro-click":"url"})
        for count in range(len(extension)):
            extensions.append("http://github.com/" + extension[count].get_text())
    return extensions


def scrape_repos(repo_urls=[]):
    '''
    This function takes in a list of urls
    and returns the language, watchers, stars, forks, commits
    and text of the readme files associated with a single url
    '''
    readme_data = []
    requests = 0
    for repo in repo_urls:
        requests += 1
        print(requests)
        repo_soup = make_soup(repo)
        if repo_soup.find('span', class_="Progress-item", itemprop='keywords', attrs='aria-label') == None:
            continue
        else:
            for sentence in repo_soup.findAll(class_="markdown-body entry-content container-lg"):
                readme = ''.join(sentence.findAll(text=True))
            language = repo_soup.find('span', class_="Progress-item", itemprop='keywords', attrs='aria-label')['aria-label']
            watchers = repo_soup.find_all('a', class_="social-count")[0].text.strip()
            stars = repo_soup.find_all('a', class_="social-count")[1].text.strip()
            forks = repo_soup.find_all('a', class_="social-count")[2].text.strip()
            commits = repo_soup.find_all('strong')[3].text
            repo_info = {'language' : language,
                     'readme': readme,
                     'watchers': watchers,
                     'stars': stars,
                     'forks': forks,
                     'commits': commits}
            readme_data.append(repo_info)
    return readme_data
    
    
    
    
    