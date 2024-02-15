import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.core import validators

is_all_posts_passive = True


def is_active_default():
    return is_all_posts_passive

# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
# alt + enter при import

# git add --all
# git commit -m "комментарий"
# git push origin lesson_07
# название ветки в конце


def validate_even(val):
    if val % 2 != 0:
        raise ValidationError('Число %(value)s нечетное',
                              code='odd',
                              params={'value':val})


# class MinMaxValueValidator:
#     def __init__(self, min_value, max_value):
#         self.min_value = min_value
#         self.max_value = max_value
#
#     def __call__(self, val):
#         if val < self.min_value or val > self.max_value:
#             raise ValidationError(
#                 'Введенное число должно находиться в диапозоне от %(min)s до %(max)s',
#                 code='out_of_range',
#                 params={'min': self.min_value, 'max': self.max_value}
#             )
#

class RubricQuerySet(models.QuerySet):
    def order_by_bb_count(self):
        # return self.annotate(
        #     cnt=models.Count('bb')).order_by('-cnt')
        return self.annotate(cnt=models.Count('bb')).order_by('-cnt')

# Диспетчер записей снизу


class RubricManager(models.Manager):
    def get_queryset(self):
        # return super().get_queryset().order_by('-order', '-name')
        return RubricQuerySet(self.model, using=self._db)

    def order_by_bb_count(self):
        return super().get_queryset().annotate(
            cnt=models.Count('bb')).order_by('-cnt')


class BbManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('price')


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True,
                            verbose_name='Название', unique=True)
    order = models.SmallIntegerField(default=0, db_index=True)
    objects = models.Manager.from_queryset(RubricQuerySet)()

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    # def delete(self, *args, **kwargs):
    #     super().delete(*args, **kwargs)

    def get_absolute_url(self):
        return f"/{self.pk}/"

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрики'
        ordering = ['order', 'name']


class Bb(models.Model):

    KINDS = (
        (None, 'Выберите тип объявления'),
        ('b', 'Куплю'),
        ('s', 'Продам'),
        ('c', 'Обменяю'),
    )

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

    rubric = models.ForeignKey("Rubric", null=True, on_delete=models.PROTECT,
                               verbose_name='Рубрика')
    title = models.CharField(
        max_length=50,
        verbose_name="Товар",
        validators=[validators.RegexValidator(regex='^.{4,}$')],
        error_messages={'invalid':'Здесь могла быть ваша реклама'}
        # validators=[validators.MinLengthValidator(4),
        #             validators.MaxLengthValidator(50)]
    )

    kind = models.CharField(max_length=1, choices=KINDS, default='s', verbose_name='Тип объявления')

    is_active_default = False

    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2, # цифры после плавающей точки
        verbose_name="Цена",
        default=0,
        # validators=[validate_even,
                    # MinMaxValueValidator(25, 45)]
    )

    is_active = models.BooleanField(default=is_active_default)
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")
    updated = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Опубликовано")

    objects = models.Manager()
    by_price = BbManager()

    def __str__(self):
        return f'{self.title}'

    def clean(self):
        errors = {}
        if not self.content:
            errors['content'] = ValidationError('Укажите описание продаваемого товара')
        if self.price and self.price < 0:
            errors['price'] = ValidationError('Укажите неотрицательное значение цены')
        if errors:
            raise ValidationError(errors)

    def clean_title(self):
        # print("Р А Б О Т А Е Т")
        errors = {}
        if self.title == "Бобер":
            errors['title'] = ValidationError('Бобры не продаются, родина в них нуждается')
        if errors:
            raise ValidationError(errors)

    def title_and_price(self):
        if self.price:
            return f'{self.title} ({self.price:2f})'
        return self.title

    title_and_price.short_description = 'Название и цена'

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявления'
        # ordering = ['-published']
        # order_with_respect_to = 'rubric'


class RevRubric(Rubric):
    class Meta:
        proxy = True
        ordering = ['-name']
