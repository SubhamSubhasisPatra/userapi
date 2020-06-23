from django.shortcuts import render

# import the HttpResponse
from django.http import HttpResponse

# Create your views here.
import json
from .models import User, ActivityPeriod


def index(request):

    response_data = {}
    response_data['ok'] = True

    # code to fetch data from your databse

    members = User.objects.values()
    members = list(members)

    for m in members:
        activities = ActivityPeriod.objects.filter(user_id=m['id']).values()
        m['activity_periods'] = [ {'start_time':x['start_time'], 'end_time':x['end_time']} for x in list(activities)]
    response_data['members'] = members

    return HttpResponse(json.dumps(response_data), content_type="application/json")
