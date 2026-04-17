from django.shortcuts import render
from .models import Event
from django.utils import timezone

def event_detail(request):
    event = Event.objects.first()

    if event:
        remaining_time = event.event_date - timezone.now()

        total_seconds = int(remaining_time.total_seconds())

        if total_seconds < 0:
            total_seconds = 0

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        data = {
            'name': event.name,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds,
        }

    else:
        data = {
            'name': "No Event",
            'hours': 0,
            'minutes': 0,
            'seconds': 0,
        }

    return render(request, 'countdown/countdown.html', {'data': data})