from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.views import APIView

from django.http import JsonResponse
from search_engine.models import SearchEngine, AjaxUserSearch
from .serializers import SearchResultSerialzer, SearchUsersSerialzer
from .sentimental_analysis import CheckMood

class AllSearchView(APIView):
    def get(self, request, *args, **kwargs):
        qs = SearchEngine.objects.all()
        serializer = SearchResultSerialzer(qs, many=True) 

        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):        
        search = request.data.get("search")
        try:
            if SearchEngine.objects.get(search=search):
                obj = SearchEngine.objects.get(search=search)
                serializer = SearchResultSerialzer(obj)
                return Response(serializer.data)
        except Exception:
            pass

        result = CheckMood(search).remove_noise()
        modified = {
            "search":search,
            "result":result,
        }
        
        serializer = SearchResultSerialzer(data=modified)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

class UserSearchView(APIView):
    def get(self, request, *args, **kwargs):
        qs = AjaxUserSearch.objects.all()
        serializer = SearchUsersSerialzer(qs, many=True) 

        return Response(data=serializer.data)

class SingleSearchView(APIView):
    def get(self, request, id):
        qs = SearchEngine.objects.filter(id=id)
        serializer = SearchResultSerialzer(qs, many=True)
        
        return Response(data=serializer.data)

class SentimentsSearchView(APIView):
    def get(self, request, *args, **kwargs):
        qs = SearchEngine.objects.all()
        serializer = SearchResultSerialzer(qs, many=True) 

        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):        
        search = request.data.get("search")        
        result = CheckMood(search).remove_noise()
        modified = {
            "search":search,
            "result":result,
        }                
        
        return JsonResponse(modified)

       