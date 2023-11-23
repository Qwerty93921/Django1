import uuid

from django.db import models

# Create your models here.
# python manage.py makemigrations

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрики'
        ordering = ['name']

class Bb(models.Model):

    # class Kinds(models.TextChoices):
    #     BUY = 'b', 'Куплю'
    #     SELL = 's', 'Продам'
    #     RENT = 'r'
    #
    # kind = models.CharField(max_length=1, choices=Kinds.choices, default=Kinds.SELL)

    # ------------------------------------------------------------------------------------------

    # KINDS = (
    #     ('Купля-продажа',(
    #         ('b', 'Куплю'),
    #         ('s', 'Продам'),
    #     )),
    #     ('Обмен', (
    #         ('c', 'Обменяю'),
    #      ))
    # )

    # ------------------------------------------------------------------------------------------

    KINDS = (
        (None, 'Выберите тип объявления'),
        ('b', 'Куплю'),
        ('s', 'Продам'),
        ('c', 'Обменяю'),
    )

    # kind = models.CharField(max_length=1, choices=KINDS, default='s')
    kind = models.CharField(max_length=1, choices=KINDS, blank=True)
    is_active_default = False
    rubric = models.ForeignKey("Rubric", null=True, on_delete=models.PROTECT,
                               verbose_name='Рубрика') # foreignKey = нижний ключ
    title = models.CharField(max_length=50, verbose_name="Товар")
    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена", default=0)
    is_active = models.BooleanField(default=is_active_default)
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")
    updated = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Опубликовано")
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # def __str__(self):
    #    pass
    # Он меняет цвет

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявления'
        ordering = ['-published']
