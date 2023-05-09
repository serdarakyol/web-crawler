from requests import get
from .base_crawler import BaseCrawler
from bs4 import BeautifulSoup
from .enum import DataEntry
import sys
# number of the order
# number of comments
class CustomCrawler(BaseCrawler):

    def __init__(self, link: str, page: int) -> None:
        super().__init__(link, page)
        self.result = {
            DataEntry.Title.value: list[str],
            DataEntry.Point.value: list[int],
            DataEntry.Rank.value: list[int],
            DataEntry.TotalCommand.value: list[str]
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
                # this will extract only the numbers from string because text contain \ character
                all_tags = list(tg.get_text(strip=True).split('|')[-1].replace("xa0comments", "").split()[0] for tg in tags)
            case _:
                print("This option is no valid=", type)
                sys.exit(1)

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
    
    def extract_total_command(self, soup:BeautifulSoup) -> None:
        span_tags = soup.find_all('span', class_='subline')
        self.extract_and_check(span_tags, DataEntry.TotalCommand)

    def start(self):
        response = get(self.link) 
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            self.extract_titles(soup)
            self.extract_points(soup)
            self.extract_total_command(soup)
        else: 
            print("FAIL", response.status_code)
        print(self.result)
