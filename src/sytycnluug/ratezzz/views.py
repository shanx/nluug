from django.shortcuts import render_to_response
from django.views.generic import  View

from .models import Talk


class TalkView(View):
    def get(self, request):
        return render_to_response('talk_list.html', {'talks': Talk.objects.all()})
