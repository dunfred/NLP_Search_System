from django.contrib import admin
from .models import SearchEngine, AjaxUserSearch

# Register your models here.
admin.site.register(SearchEngine)
admin.site.register(AjaxUserSearch)