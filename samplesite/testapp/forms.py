from django import forms

from .models import Img


class ImgForm(forms.ModelForm):
    img = forms.ImageField(label='Изображение')
    desc = forms.CharField(label='Описание',
                           widget=forms.widget.Textarea())

    class Meta:
        model = Img
        fields = '__all__'
