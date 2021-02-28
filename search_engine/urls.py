from django.urls import path, include
from django.conf.urls import url
from .views import (user_search_view, 
                    sentiments_search_view, 
                    list_users,
                    create_user)

urlpatterns = [    
    path("api/", include("search_engine.api.urls")),    
    path("", list_users, name="list-users"),
    path("create/", create_user, name="create-user"),
    path("update/", list_users, name="update-user"),
    path("delete/", list_users, name="delete-user"),
    path("students/", user_search_view, name="search-users"),
    path("sentiments/", sentiments_search_view, name="sentiments-data"),
]