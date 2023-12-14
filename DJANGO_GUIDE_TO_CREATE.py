# Python -m venv venv
# venv/Scripts/activate
# pip install django
# django-admin startproject samplesite

# https://django.fun/docs/django/4.2/topics/migrations/#the-commands

# ----------------------------------------------------------------------------------------------------------------

# git checkout -b lesson_11
# Создание новой ветки и переключение на нее

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

# -----------------------------------------------------------------------------------------------------------------------------------------

# LESSON_09

# python manage.py shell
# (вызов консоли, exit(), quit() - выход из нее)
#
# b = Bb.objects.get(pk=21)
#
# b вызвать(перезаписано)
#
# b.title = 'Бобер ездовой'
# b.content = 'Огромный'
# b.price = 100000
# b.save()
# (сохранение b)
#
#
# --------------------------------------------------------------------------
# from bboard.models import Bb
# (если не работает)
#
# from bboard.models import Rubric
# r = Rubric()
# r.name = 'Бытовая техника'
# r.save()
# r = Rubric(name='Сельхозтехника')
# r.save()
# r = Rubric.objects.create(name='Мебель')
# r
# (Мебель должно высветиться)
#
#
# r.pk
# 3(выдает)
#
#
# Rubric.objects.get_or_create(name='Мебель')
# Rubric.objects.get_or_create(name='Цветы')
# Rubric.objects.get_or_create(name='Сантехника')
#
# Rubric.objects.update_or_create(name='Цветы', defaults={'name': 'Растения'}
#
# b = Bb.objects.get(pk=21)
# b.kind
#
# b.title = 'Бобер необъезженный'
# b.save(update_fields=['title'])
#
# --------------------------------------------------------------------------------------------------
# python manage.py shell
# (в консоли)
#
# from bboard.models import Bb
# b = Bb.objects.get(title='fg35353')
#
# b.delete()
#
# from bboard.models import Rubric
# r = Rubric.objects.get(name='Недвижимость')
#
# b = Bb()
# b.title='Телевышка'
# b.content='345 метров'
# b.price = 1050
# b.rubric = r
# b.save()
#
# r = Rubric.objects.create(name='Сельхозинвентарь')
# b = Bb.objects.create(title='Мотыга')
#
# b = Bb.objects.create(title='Мотыга', content='Ржавая', price=20)
# b.title = 'Мотыга'
#
# b.save()
# r.bb_set.add(b)
#
# b.rubric
# (Выходит - Сельхозинвентарь)
#
# >>> b2 = r.bb_set.create(title='Лопата', content='Почти новая', price=1000)
# >>> b2.rubric
# (<Rubric: Сельхозинвентарь>) - выходит
#
# from testapp.models import AdvUser
#
# >>> from django.contrib.auth.models import User
# >>> from testapp.models import AdvUser
# >>> from django.contrib.auth.models import User
# >>> u = User.objects.get(username='admin')
#
# >>> au = AdvUser.objects.create(user=u)
#
# au = AdvUser.objects.create(user=u)
# >>> au.user
# <User: admin>
# >>> u.advuser
# <AdvUser: AdvUser object (1)>
# >>> au2 = AdvUser.objects.get(pk=1)
# >>> u.advuser = au2
# >>> u.save()
# >>> u.advuser
# <AdvUser: AdvUser object (1)>
#
# pk - primary key(первичный ключ)

# ----------------------------------------------------------------------------------------------------------------

# python manage.py shell
#
# (Все что далее это из консоли)
#
# from bboard.models import Rubric, Bb
# r = Rubric.objects.get(name='Сельхозинвентарь')
# r.get_bb_order()
# <QuerySet [2, 3]>(само выходит)
# r.set_bb_order([3, 2])
# r.get_bb_order()
# <QuerySet [3, 2]>(само выходит)
#
# (меняет местами ID и расположение вещей в списке)
#
#
# Bulk_create(создать толпу) - сразу много значений за одну команду добавляется
# bulk_update
#
# Bb.objects.bulk_create([Bb(title='Пылесос', content='Хороший, мощный', price=1000, rubric=r), Bb(title='Стиральная машина', content='Автоматическая', price=1000, rubric=r)])
#
#
# Операции сравнения в запросах
# lt = less than
# Bb.objects.filter(price__lt=40).update(price=40)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# b = Bb.objects.filter(price__gte=10_000).first()
# gte - greater than equal
#
# for b in Bb.objects.order_by('rubric__name', '-price'):
# ...     print(b.title)
#
# тире перед словом означает ОБРАТНЫЙ ПОРЯДОК

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# lesson_12

# В КОНСОЛИ(shell)

# Bb.objects.values('title', 'price', 'rubric')
# выводит в виде СЛОВАРЯ: название, цену и рубрику
#
#
# Bb.objects.values_list('title', 'price', 'rubric')
# выводит в виде КОРТЕЖА: название, цену и рубрику
