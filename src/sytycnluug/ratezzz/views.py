from django.http import HttpResponse
from django.views.generic import  View


class TalkView(View):
    def get(self, request):
        return HttpResponse()
