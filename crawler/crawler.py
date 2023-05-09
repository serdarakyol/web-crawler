from requests import get
from .base_crawler import BaseCrawler
from bs4 import BeautifulSoup
from .enum import DataEntry
# number of the order
# number of comments
class CustomCrawler(BaseCrawler):

    def __init__(self, link: str, page: int) -> None:
        super().__init__(link, page)
        self.result = {
            DataEntry.Title.value: list[str],
            DataEntry.Point.value: list[int],
            DataEntry.Rank.value: list[int],
            DataEntry.TotalCommand.value: list[int]
        }

    def extract_and_check(self, tags:BeautifulSoup, type:str) -> None:
        match type:
            case DataEntry.Title:
                all_tags = list(tg.get_text(strip=True) for tg in tags)
            case DataEntry.Point:
                all_tags = list(int(tg.get_text(strip=True).replace(" points", "")) for tg in tags)
            case DataEntry.Rank:
                print("RANK")
            case DataEntry.TotalCommand:
                print("TOTAL COMMAND")

        # check if all tags extracted
        if len(all_tags) == 30:
            print(f"{type.value} Successfully extracted")
        else:
            print(f"All {type.value} could not extract")
        self.result[type.value] = all_tags
    
    def extract_titles(self, soup:BeautifulSoup) -> None:
        span_tags = soup.select('span.titleline > a')
        self.extract_and_check(span_tags, DataEntry.Title)
        
    def extract_points(self, soup:BeautifulSoup) -> None:
        span_tags = soup.find_all('span', class_='score')
        self.extract_and_check(span_tags, DataEntry.Point)

    def start(self):
        response = get(self.link) 
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            self.extract_titles(soup)
            self.extract_points(soup)
        else: 
            print("FAIL", response.status_code)
        print(self.result)
