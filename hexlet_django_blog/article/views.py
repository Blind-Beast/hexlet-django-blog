from django.shortcuts import render

from django.http import HttpResponse
from django.views import View


class IndexView(View):
    def get(self, request, article_id, tags):
        return HttpResponse(f"Статья номер {article_id}. Тег {tags}")