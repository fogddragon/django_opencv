from django import forms
from opcv.models import Image


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['image', 'title']


class ImageEditForm(forms.Form):

    treshold = forms.IntegerField(label='value of treshold', max_value=255)
    medianblur = forms.BooleanField()

