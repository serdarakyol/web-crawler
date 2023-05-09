from crawler.crawler import CustomCrawler
from utils.extract_file import JsonToCsv
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-l', '--link', help='Link of website', required=True)
    parser.add_argument('-p', '--page', help='Number of page')
    parser.add_argument('-o', '--output', help='Output file directory')
    parser.add_argument('-f', '--filename', help='Name of the file to be generated')
    
    args = parser.parse_args()

    crawler = CustomCrawler(args.link, args.page)
    json_object = crawler.start()
    saver = JsonToCsv(json_object, args.output, args.filename)
    saver.generate_csv()
    
