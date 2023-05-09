class BaseCrawler:
    def __init__(self, link:str, page:int) -> None:
        self.link = link
        self.page = page
