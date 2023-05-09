from typing import Any
from requests import get
from .base_crawler import BaseCrawler
from bs4 import BeautifulSoup
# title
# number of the order
# number of comments
# points
class CustomCrawler(BaseCrawler):

    def __init__(self, link: str, page: int) -> None:
        super().__init__(link, page)
        self.result = {
            "Title": list[str],
            "Rank": list[int],
            "TotalCommand": list[int],
            "Points": list[int]
        }
    
    def extract_titles(self, content) -> int:
        soup = BeautifulSoup(content, 'lxml')
        td_tags = soup.select('span.titleline > a')
        
        # best practice for memory allocation
        all_titles = list(td.get_text(strip=True) for td in td_tags)
        self.result["Title"] = all_titles
        
        if len(all_titles) == 30:
            print("Titles are succesfully extracted")
        else:
            print("All titles are not extracted successfuly")

    def start(self):
        response = get(self.link) 
        if response.status_code == 200:
            self.extract_titles(response.text)
        else: 
            print("FAIL", response.status_code)
