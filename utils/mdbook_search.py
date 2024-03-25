import urllib.parse
import yaml
from selenium import webdriver  # Installed
from selenium.webdriver.chrome.options import Options  # Installed
from bs4 import BeautifulSoup as Soup  # Installed

with open("config.yaml", "r") as cfg_yaml:
    cfg = yaml.safe_load(cfg_yaml)

# Setup Selenium Webdriver
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

mdBook_url = cfg["mdBook"]["mdBookHomeURL"]


class SearchResult(dict):
    def __init__(self, title, href, paragraph_preview):
        dict.__init__(self, title=title, href=href, paragraph_preview=paragraph_preview)


def url_string(string):
    return urllib.parse.quote(string, '/#?=')


def get_html(url):
    driver.get(url)
    return driver.page_source


def get_processed_results(query_url):
    html_item = Soup(get_html(query_url), 'html.parser')
    results_ul = html_item.find("ul", id="searchresults")
    results = results_ul.find_all('li')
    processed_results = []
    for result in results:
        title = result.a.get_text()
        result_href = query_url[0:query_url.find("?")] + url_string(result.a['href'])
        paragraph_preview = result.span.get_text()
        process_result = SearchResult(title, result_href, paragraph_preview)
        processed_results.append(process_result)
    return processed_results


def search_wiki(query):
    query_url = mdBook_url + "?search=" + url_string(query)
    return get_processed_results(query_url)
