# Web scrapper
This repository mainly extract data from `https://news.ycombinator.com/`. Alternatively, can be modified for other web pages too. After installation, you can send link, page, customize output directory and filename. The reason for not using a database in this project is that the project is small. Used `csv` file instate of database.

## How to use
Download the repository and run below command to install requirements
```bash
pip install -r requirements.txt
```

Send request
```bash
python3 main.py -l 'https://news.ycombinator.com/'
```
