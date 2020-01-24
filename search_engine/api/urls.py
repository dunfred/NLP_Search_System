from django.urls import path
from .views import (AllSearchView, 
                    SingleSearchView, 
                    UserSearchView,
                    SentimentsSearchView)

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", AllSearchView.as_view(), name='all-searches'),
    path('<int:id>/', SingleSearchView.as_view(), name='single-search-details'),
    path('users/', UserSearchView.as_view(), name='user-api-details'),
    path('sentiments/', SentimentsSearchView.as_view(), name='sentiments-api-details'),
]