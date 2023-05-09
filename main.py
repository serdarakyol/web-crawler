from crawler.crawler import CustomCrawler
from argparse import ArgumentParser


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-l', '--link', help='Link of website')
    parser.add_argument('-p', '--page', help='Number of page')
    
    args = parser.parse_args()

    crawler = CustomCrawler(args.link, args.page)
    crawler.start()
    
