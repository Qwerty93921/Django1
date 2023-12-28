from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.loader import get_template, render_to_string
from django.urls import reverse_lazy, reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .forms import BbForm
from .models import Bb, Rubric


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.annotate(cnt=Count('bb')).filter(cnt__gt=0)
    context = {'bbs': bbs, 'rubrics': rubrics}
    # template = get_template('index.html')
    # return HttpResponse(
    #     # template.render(context=context, request=request))
    #     template.render(context, request))

    return HttpResponse(
        render_to_string('index.html', context, request)
    )


# def index_1(request):
#     response = HttpResponse("Здесь будет",
#                             content_type='text/plain; charset=utf-8')
#     response.write(' главная')
#     response.writelines((' страница', ' сайта'))
#     response['keywords'] = 'Python, Django'
#     return response


# python manage.py runserver
# в консоли писать это
# ctrl + c - выход
# exit()
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver



# def index_0(request):
#     bbs = Bb.objects.order_by('-published')
#     # rubrics = Rubric.objects.filter(bb__isnull=False).distinct()
#     rubrics = Rubric.objects.annotate(cnt=Count('bb')).filter(cnt__gt=0)
#     context = {'bbs': bbs, 'rubrics':rubrics}
#     return render(request, 'index.html', context)


# def by_rubric(request, rubric_id):
#     bbs = Bb.objects.filter(rubric=rubric_id)
#     rubrics = Rubric.objects.filter(bb__isnull=False).distinct()
#     current_rubric = Rubric.objects.get(pk=rubric_id)
#     context = {'bbs':bbs, 'rubrics':rubrics,
#                'current_rubrics':current_rubric}
#     return render(request, 'by_rubric.html', context)



class BbByRubricView(TemplateView):
    template_name = 'by_rubric.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bbs'] = Bb.objects.filter(rubric=context['rubric_id'])
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(pk=context['rubric_id'])
        return context


# def add(request):
#     bbf = BbForm()
#     context = {'form': bbf}
#     return render(request, 'create.html', context)
#
#
# def add_save(request):
#     bbf = BbForm(request.POST)
#
#     if bbf.is_valid():
#         bbf.save()
#         return HttpResponseRedirect(
#             reverse('bboard:by_rubric'),
#             kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}
#         )
#     else:
#         context = {'form': bbf}
#         return render(request, 'create.html', context)


# def add_and_save(request):
#     print(request.headers['Accept-Encoding'])
#     print(request.headers['accept-encoding'])
#     print(request.headers['accept_encoding'])
#     print(request.headers['Cookie'])
#     print(request.resolver_match)
#     print(request.body)
#
#     if request.method == 'POST':
#         bbf = BbForm(request.POST)
#         if bbf.is_valid():
#             bbf.save()
#             return HttpResponseRedirect(
#                 reverse('bboard:by_rubric',
#                 kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk})
#             )
#         else:
#             context = {'form': bbf}
#             return render(request, 'create.html', context)
#     else:
#         bbf = BbForm()
#         context = {'form': bbf}
#         return render(request, 'create.html', context)


class BbCreateView(CreateView):
    template_name = 'create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # key word arguments, kwargs - ключ значение, args - набор значений
        context['rubrics'] = Rubric.objects.annotate(cnt=Count('bb')).filter(cnt__gt=0)
        return context


def details(request, bb_id):
    try:
        bb = Bb.objects.get(pk=bb_id)
    except Bb.DoesNotExist:
        raise Http404()
    return HttpResponse()


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
