from django.core.exceptions import NON_FIELD_ERRORS
from django.core.paginator import Paginator
from django.db.models import Count
from django.forms.formsets import ORDERING_FIELD_NAME
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.template.loader import get_template, render_to_string
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import FormView, ArchiveIndexView, MonthArchiveView, RedirectView
from django.forms import modelformset_factory

# FormView, ArchiveIndexView, MonthArchiveView

from .forms import BbForm, RubricBaseFormSet
from .models import Bb, Rubric


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.annotate(cnt=Count('bb')).filter(cnt__gt=0)

    paginator = Paginator(bbs, 2, orphans=2)

    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1

    page = paginator.get_page(page_num)

    context = {'rubrics': rubrics, 'page_obj': page, 'bbs': page.object_list}

    # template = get_template('index.html')
    # return HttpResponse(
    #     # template.render(context=context, request=request))
    #     template.render(context, request))

    return render(request, 'index.html', context)

# class BbIndexView(ArchiveIndexView):
#     model = Bb
#     template_name = 'index.html'
#     date_field = 'published'
#     date_list_period = 'month'
#     month_format = '%m'
#     context_object_name = 'bbs'
#     allow_empty = True
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['rubrics'] = Rubric.objects.all()
#         return context


class BbIndexView(ListView):
    model = Bb
    template_name = 'index.html'
    context_object_name = 'bbs'
    paginate_by = 2

    def get_queryset(self):
        return Bb.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.annotate(cnt=Count('bb')).filter(cnt__gt=0)


class BbMonthView(MonthArchiveView):
    model = Bb
    template_name = 'index.html'
    date_field = 'published'
    date_list_period = 'month'
    month_format = '%m'
    context_object_name = 'bbs'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

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


class BbByRubricView(ListView):
    template_name = 'by_rubric.html'
    context_object_name = 'bbs'

    def get_queryset(self):
        return Bb.objects.filter(rubric=self.kwargs['rubric_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(
            pk=self.kwargs['rubric_id'])
        return context


class BbAddView(FormView):
    template_name = 'create.html'
    form_class = BbForm
    initial = {'price': 0.0}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object

    def get_success_url(self):
        return reverse('bboard:by_rubric',
                       kwargs={'rubric': self.object.cleaned_data['rubric.'].pk})


class BbDetailView(DetailView):
    model = Bb

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BbEditView(UpdateView):
    model = Bb
    form_class = BbForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubric'] = Rubric.objects.all()
        return context


class BbDeleteView(DeleteView):
    model = Bb
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubric'] = Rubric.objects.all()
        return context



# class BbByRubricView(TemplateView):
#     template_name = 'by_rubric.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['bbs'] = Bb.objects.filter(rubric=context['rubric_id'])
#         context['rubrics'] = Rubric.objects.all()
#         context['current_rubric'] = Rubric.objects.get(pk=context['rubric_id'])
#         return context


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
    success_url = '/'
    # success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # key word arguments, kwargs - ключ значение, args - набор значений
        context['rubrics'] = Rubric.objects.annotate(cnt=Count('bb')).filter(cnt__gt=0)
        return context


# def details(request, bb_id):
#     try:
#         bb = Bb.objects.get(pk=bb_id)
#     except Bb.DoesNotExist:
#         raise Http404()
#     return HttpResponse()


# def index_old(request):
#     template = loader.get_template('index.html')
#     bbs = Bb.objects.order_by('-published')
#     context = {'bbs': bbs}
#     return HttpResponse(template.render(context, request))

    # s = 'Список объявлений\r\n\r\n\r\n'
    #
    # for bb in Bb.objects.order_by('-published'):
    #     s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    # return HttpResponse(s, content_type='text/plain; charset=utf-8')

def edit(request, pk):
    bb = Bb.objects.get(pk=pk)

    if request.method == 'POST':
        bbf = BbForm(request.POST, instance=bb)
        if bbf.is_valid():
            if bbf.has_changed():
                bbf.save()
            return HttpResponseRedirect(
                reverse('bboard:by_rubric',
                        kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk})
            )
        else:
            context = {'form' : bbf}
            return render(request, 'bboard/bb_form.html', context)
    else:
        bbf = BbForm(instance=bb)
        context = {'form': bbf}
        return render(request, 'bboard/bb_form.html', context)


def add_save(request):
    bbf = BbForm(request.POST)

    if bbf.is_valid():
        bbf.save()
        return HttpResponseRedirect(
            reverse('bboard:by_rubric',
                    kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk})
        )
    else:
        context = {'form': bbf}
        return render(request, 'bboard/bb_form.html', context)


def rubrics(request):
    RubricFormSet = modelformset_factory(Rubric, fields=('name',),
                                         can_order=True, can_delete=True, extra=3, formset=RubricBaseFormSet)

    if request.method == 'POST':
        formset = RubricFormSet(request.POST)

        if formset.is_valid():
            instances = formset.save(commit=False)
            for obj in formset:
                if obj.cleaned_data:
                    rubric = obj.save(commit=False)
                    rubric.order = formset.cleaned_data[ORDERING_FIELD_NAME]
                    rubric.save()

            for obj in formset.deleted_objects:
                obj.delete()

            return redirect('bboard:rubrics')

    else:
        formset = RubricFormSet()

    context = {'formset': formset}

    return render(request, 'bboard/rubrics.html', context)
