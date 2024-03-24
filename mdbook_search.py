import urllib.parse
from selenium import webdriver  # Installed
from selenium.webdriver.chrome.options import Options  # Installed
from bs4 import BeautifulSoup as Soup  # Installed

# Setup Selenium Webdriver
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)