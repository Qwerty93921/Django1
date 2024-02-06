"""
URL configuration for samplesite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import (# index,
                    BbIndexView, BbByRubricView, BbCreateView,
                    BbDetailView, BbAddView, BbEditView, BbDeleteView, BbMonthView,
                    RedirectView, edit, rubrics
                    )

# Скобки потому что много строк, если 1 СТРОКА, тогда БЕЗ СКОБОК

app_name = 'bboard'

urlpatterns = [
    # path('add/', BbCreateView.as_view(), name='add'),

    # path('add/save/', add_save, name='add_save'),

    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('add/', BbAddView.as_view(), name='add'),

    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),
    # path('', index, name='index'),
    path('', BbIndexView.as_view(), name='index'),
    path('year/<int:year>/', RedirectView.as_view(), name='redirect'),
    path('<int:year>/<int:month>/', BbMonthView.as_view(), name='month'),
    path('update/<int:pk>/', edit, name='update'),
    path('delete/<int:pk>/', BbDeleteView.as_view(), name='delete'),

    path('rubrics/', rubrics, name='rubrics'),
]
