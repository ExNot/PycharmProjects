from django.shortcuts import render

from . import articles
from .articles import Articles

def article_list(request):  #article başlıklarının listelendiği sayfa
    a1s = articles.Articles #articles nesneleri değişkene atandı
    return render(request, "article_list.html", {'article_list': a1s}) #dict türünde article_list.html'e gönderildi

def article_detail(request,title):  #article içeriğinin görüntülendiği sayfa
    a1s = articles.Articles
    return render(request, 'article_detail.html', {'article': a1s[title]})