import requests
from bs4 import BeautifulSoup
from .models import News


def get_news():

    # ria_news = requests.get('https://ria.ru/')
    # rbc_news = requests.get('https://www.rbc.ru/short_news')
    # lenta_news = requests.get('https://lenta.ru/')
    # ria_soup = BeautifulSoup(ria_news.text, 'html.parser')
    # rbc_soup = BeautifulSoup(rbc_news.text, 'html.parser')
    # lenta_soup = BeautifulSoup(lenta_news.text, 'html.parser')

    # newspaper_soup = BeautifulSoup(newspaper_news.text, 'html.parser')
    # newspaper_titles = newspaper_soup.findAll('div', class_='b_ear-textblock')
    # for new in newspaper_titles:
    #     News.objects.create(content=new.find('div', class_='b_ear-title').text.strip())
    pass
