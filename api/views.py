from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
import random

def what_am_i_doing(request):
    now = datetime.now()
    hour = now.hour
    weekday = now.weekday()

    if 0 <= hour < 6:
        message = random.choice(["Probably asleep", "Dreaming of code", "Dead to the world"])
    elif 9 <= hour <= 17 and weekday < 5:
        message = random.choice(["Working", "Probably in a meeting", "Writing Python code"])
    elif hour >= 22:
        message = random.choice(["Watching Netflix", "Gaming", "Reading in bed"])
    elif weekday >= 5:
        message = random.choice(["Weekend vibes", "Relaxing", "Out and about"])
    else:
        message = "Probably doing something random"

    return JsonResponse({"message": message})