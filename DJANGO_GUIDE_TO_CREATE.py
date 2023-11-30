# Python -m venv venv
# venv/Scripts/activate
# pip install django
# django-admin startproject samplesite

# https://django.fun/docs/django/4.2/topics/migrations/#the-commands

# ----------------------------------------------------------------------------------------------------------------

# GIT PUSH GUIDE

# python manage.py startapp название папки
#
# git add --all
# git commit -m "комментарий"
# git push origin lesson_06
#
# origin - это название репозитория
# lesson_06 - название ветки

# ----------------------------------------------------------------------------------------------------------------

# python -m venv venv
# .\venv\Scripts\activate
# pip install django
#
# pip list
# Проверить
#
# django-admin startproject myapp(название)
# сделать папку синей(source root)
#
# python manage.py startapp first_app
# внутри папки с проектом
#
# settings открыть и переименовать в кавычках в INSTALLED_APPS ['first_app']
# В urls(myapp) менять в URLPATTERNS path НИЖНИЙ
#
# urlpatterns = [
# 	path('admin', )
# 	path('', include('firstapp_urls', namespace='first_app')),
# ]
#
# В views добавить
#
# def index(request):
# 	context = {
# 		"var":"value"
# }
#
# return render(requst, '')
#
#
# B settings менять TEMPLATES = [{DIRS: [BASE_DIR 'templates'],
#  }]

# git branch - показывает СКОЛЬКО ВЕТОК
# git chekout -b lesson_08
# Создание ветки и название

# python manage.py makemigrations
# python manage.py migrate название если нужно

# python manage.py makemigrations название если нужно после этого ЛИБО НЕ ПИСАТЬ
# python manage.py makemigrations -n название следующей миграции(вместо длинного названия будет то которое указал пользователь)
# Можно менять название ВРУЧНУЮ только если файл ЕЩЕ НЕ ИСПОЛЬЗОВАЛСЯ, если использовался УЖЕ, ТОГДА НЕТ

# python manage.py --merge
# Ищет ошибки и пытается соединить файлы в 1 файл

# python manage.py squashmigrations bboard(название) 0003
# Соединяет все файлы МИГРАЦИИ до номера ВКЛЮЧИТЕЛЬНО в ОДИН ФАЙЛ(От 0001 до 0003)


# python manage.py showmigrations bboard(название)

# dump - туда
# load - обратно

