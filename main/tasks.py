from aggregator.celery import app
import requests
from bs4 import BeautifulSoup
from .models import News


@app.task
def get_news_task():
    ria_news = requests.get('https://ria.ru/')
    ria_soup = BeautifulSoup(ria_news.text, 'html.parser')
    ria_titles = ria_soup.findAll('span', class_='cell-list__item-title')
    for ria_new in ria_titles:
        News.objects.create(site='РИА',
                            content=ria_new.text.strip())

    rbc_news = requests.get('https://www.rbc.ru/')
    rbc_soup = BeautifulSoup(rbc_news.text, 'html.parser')
    rbc_main_titles = rbc_soup.findAll('span', class_='main__feed__title')
    rbc_item_titles = rbc_soup.findAll('span', class_='item__title')
    for rbc_new in rbc_main_titles:
        News.objects.create(site='РБК',
                            content=rbc_new.text.strip())
    for rbc_item_new in rbc_item_titles:
        News.objects.create(site='РБК',
                            content=rbc_item_new.text.strip())

    newspaper_news = requests.get('https://www.gazeta.ru/')
    newspaper_soup = BeautifulSoup(newspaper_news.text, 'html.parser')
    newspaper_titles = newspaper_soup.findAll('div', class_='b_ear-textblock')
    for new in newspaper_titles:
        News.objects.create(site='Газета',
                            content=new.find('div', class_='b_ear-title').text.strip())

    lenta_news = requests.get('https://lenta.ru/')
    lenta_soup = BeautifulSoup(lenta_news.text, 'html.parser')
    lenta_titles = lenta_soup.findAll('span', class_='card-mini__title')
    for lenta_new in lenta_titles:
        News.objects.create(site='Лента',
                            content=lenta_new.text.strip())


