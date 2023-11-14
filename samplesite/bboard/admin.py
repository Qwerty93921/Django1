from django.contrib import admin

from .models import Bb, Rubric
# Register your models here.

class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'published', 'rubric')
    list_display_links = ('title',) # если в кортеже 1 переменная тогда запятая в конце
    search_fields = ('title', 'content')

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
