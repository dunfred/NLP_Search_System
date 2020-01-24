from rest_framework import serializers
from search_engine.models import SearchEngine, AjaxUserSearch

class SearchResultSerialzer(serializers.ModelSerializer):
    class Meta:
        model =SearchEngine
        fields = ['id',
            'search',
            'result',
        ]        

class SearchUsersSerialzer(serializers.ModelSerializer):
    class Meta:
        model =AjaxUserSearch
        fields = ['username',
                'location',
                'avatar',
        ]    

class SearchQuerySerializers(serializers.ModelSerializer):
    class Meta:
        model = SearchEngine
        fields = [
            'id',
            'search',
            'result',
        ]

        read_only_fields = [
            'id',
            'result',            
        ]


    def validate_search(self, new_search):
        qs = SearchEngine.objects.filter(search__iexact=new_search)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This Search already exists!")
        return new_search