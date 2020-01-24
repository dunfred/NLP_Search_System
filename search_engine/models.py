from django.db import models

# Create your models here.
class SearchEngine(models.Model):
    search = models.CharField(null=False, blank=True, max_length=500)
    result = models.CharField(null=False, blank=True, max_length=5000)

    class Meta:
        verbose_name_plural = "searches"

    def __str__(self):
        return self.search

class AjaxUserSearch(models.Model):
    username = models.CharField(null=False, blank=True, max_length=500)
    location = models.CharField(null=False, blank=True, max_length=5000)
    avatar   = models.ImageField(upload_to="avatars/%b")

    class Meta:
        verbose_name_plural = "Ajax User Searches"

    def __str__(self):
        return self.username 

