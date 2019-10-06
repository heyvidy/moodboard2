from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from moodlog.models import *
import json
from django.core import serializers


def home(request):
    return render(request, "home.html")


def get_moods(request):
    moods = Mood.objects.all()

    payload = []
    for mood in moods:
        payload.append({"id": mood.id, "name": mood.name, "emoji": mood.emoji})

    payload = json.dumps(payload)

    return HttpResponse(payload, content_type="application/json")


def get_actions(request):
    actions = Action.objects.all()

    payload = []
    for action in actions:
        payload.append(
            {"id": action.id, "name": action.name, "emoji": action.emoji})

    payload = json.dumps(payload)

    return HttpResponse(payload, content_type="application/json")


def get_logs(request):
    logs = MoodLog.objects.all()
    moodlogs = serializers.serialize(
        'json', logs,
        use_natural_foreign_keys=True,
        use_natural_primary_keys=True,
        indent=3)
    return HttpResponse(moodlogs, content_type="application/json")
