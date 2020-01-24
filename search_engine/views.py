from django.shortcuts import render
# from django.db.models import Q
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import generics, mixins
# from .api.serializers import SearchQuerySerializers
# from .permissions import IsOwnerOrReadOnly
from .models import AjaxUserSearch
from .forms import UserModelForm
from django.views.generic import View
from django.http import JsonResponse

# # Create your views here.
def user_search_view(request):
    template = "search_students.html"
    context = {}

    return render(request, template, context)

def sentiments_search_view(request):
    template = "search_sentiments.html"
    context = {}

    return render(request, template, context)

def list_users(request):
    users     = AjaxUserSearch.objects.all()
    form = UserModelForm()
    template  = "crud.html"
    context   = {
        "users":users,
        "form" : form,
    }

    return render(request, template, context)

def create_user(request):
    obj = AjaxUserSearch.objects.all()[0]
    data = {
            "user" : {"username":obj.username,
                      "location":obj.location,
                      "avatar":obj.avatar.name, }
        }
    if request.method == 'POST':
        form = UserModelForm(request.POST or None)
        username  = request.POST.get("username")
        location  = request.POST.get("location")
        avatar    = request.POST.get("avatar")

        print(request.FILES)
        #print(request.FILES['avatar'])

        user_obj = AjaxUserSearch.objects.create(
            username = username,
            location  = location,
            avatar    = avatar,
        )
        print(user_obj.avatar.name)
        user = {
            "id"       : user_obj.id,
            "username" : user_obj.username,
            "location" : user_obj.location,
            "avatar"   : user_obj.avatar.name,
        }

        data = {
            "user" : user,
        }

    return JsonResponse(data)

# class SearchAPIView(mixins.CreateModelMixin, generics.ListAPIView):    
#     lookup_field = 'id'
#     serializer_class = SearchQuerySerializers
#     def get_queryset(self):
#         qs = SearchEngine.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(Q(search__icontains=query)|
#                            Q(result__icontains=query)).distinct()
#         return qs

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class SearchRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):    
#     lookup_field = 'id'
#     serializer_class = SearchQuerySerializers
#     permission_classes = [IsOwnerOrReadOnly]
#     def get_queryset(self):
#         return SearchEngine.objects.all()

