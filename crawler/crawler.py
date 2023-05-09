from requests import get
from .base_crawler import BaseCrawler
from bs4 import BeautifulSoup
# title
# number of the order
# number of comments
# points
class CustomCrawler(BaseCrawler):

    def _get_title(self):
        pass
    
    def extract_tbody(self, content):
        soup = BeautifulSoup(content, 'lxml')
        td_tags = soup.find_all('td', class_='title')
        for td in td_tags:
            print(td)
            print('\n')


    def start(self):
        response = get(self.link)
        if response.status_code == 200:
            self.extract_tbody(response.text)
        else: 
            print("FAIL", response.status_code)
