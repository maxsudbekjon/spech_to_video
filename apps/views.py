from django.shortcuts import render
from django.conf import settings


def home(request):
    videos = [
        {"name": "easter_egg", "url": f"{settings.MEDIA_URL}videos/easter_egg.mp4"},
        {"name": "fallback", "url": f"{settings.MEDIA_URL}videos/fallback.mp4"},
        {"name": "general_response", "url": f"{settings.MEDIA_URL}videos/general_response.mp4"},
        {"name": "goodbye", "url": f"{settings.MEDIA_URL}videos/goodbye.mp4"},
        {"name": "greeting", "url": f"{settings.MEDIA_URL}videos/greeting.mp4"},
        {"name": "idle", "url": f"{settings.MEDIA_URL}videos/idle.mp4"},
        {"name": "listening", "url": f"{settings.MEDIA_URL}videos/listening.mp4"},
        {"name": "prompt", "url": f"{settings.MEDIA_URL}videos/prompt.mp4"},
        {"name": "weather", "url": f"{settings.MEDIA_URL}videos/weather.mp4"},
    ]
    return render(request, "home/index.html", {"videos": videos})
