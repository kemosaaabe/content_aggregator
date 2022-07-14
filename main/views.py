from django.shortcuts import render
from .service import get_news
from .tasks import get_news_task
from .models import News


def index(request):
    gazeta_news = News.objects.filter(site='Газета')
    ria_news = News.objects.filter(site='РИА')
    rbc_news = News.objects.filter(site='РБК')
    lenta_news = News.objects.filter(site='Лента')
    context = {'gazeta_news': gazeta_news[:10],
               'ria_news': ria_news[:10],
               'rbc_news': rbc_news[:10],
               'lenta_news': lenta_news[:10]}
    return render(request, 'main/index.html', context)
