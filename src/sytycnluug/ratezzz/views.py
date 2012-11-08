from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils.crypto import get_random_string
from django.views.generic import  View

from .models import Talk

RATER_COOKIE = 'rater_id'


class TalkView(View):
    def get(self, request):
        return render_to_response('talk_list.html', {'talks': Talk.objects.all()})

    def post(self, request, pk):
        rater_id = request.COOKIES.get(RATER_COOKIE, get_random_string())

        talk = Talk.objects.get(pk=pk)
        rating, is_created = talk.rating_set.get_or_create(rater_id=rater_id,
            defaults={'rating': request.POST['rating']})

        if not is_created:
            rating.rating = request.POST['rating']
            rating.save()

        response = HttpResponse()
        response.set_cookie(RATER_COOKIE, rater_id)
        return response
