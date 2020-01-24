from django import forms
from django.forms import ModelForm
from .models import SearchEngine, AjaxUserSearch

class SearchEngineForm(ModelForm):
    model = SearchEngine
    fields = ['search','result']

class UserModelForm(ModelForm):
    class Meta:
        model = AjaxUserSearch
        fields = "__all__"