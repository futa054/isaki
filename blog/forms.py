from django import forms

from .models import Blog

from django.contrib.auth.models import User

class BlogForm(forms.ModelForm):

    content = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Blog
        fields = ["content", "image", ]

class SearchForm(forms.Form):
    fromDate = forms.DateField(
        initial='',
        label='From',
        required = False,
        widget=forms.DateInput(attrs={"type":"date"}),
    )
    toDate = forms.DateField(
        initial='',
        label='To',
        required=False,
        widget=forms.DateInput(attrs={"type":"date"}),
    )
    postedBy = forms.ModelChoiceField(
        User.objects,
        label='PostedBy',
        required = False,
        empty_label='All User',
    )