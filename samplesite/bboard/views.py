from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from bboard.models import Bb

# python manage.py runserver
# в консоли писать это
# ctrl + c - выход
# exit()


def index(request):
    bbs = Bb.objects.order_by('-published')
    context = {'bbs': bbs}
    return render(request, 'index.html', context)


def index_old(request):
    template = loader.get_template('index.html')
    bbs = Bb.objects.order_by('-published')
    context = {'bbs': bbs}
    return HttpResponse(template.render(context, request))

    # s = 'Список объявлений\r\n\r\n\r\n'
    #
    # for bb in Bb.objects.order_by('-published'):
    #     s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    # return HttpResponse(s, content_type='text/plain; charset=utf-8')
