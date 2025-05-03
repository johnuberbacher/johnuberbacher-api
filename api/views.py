from django.http import JsonResponse
import random
from datetime import datetime
from .models import ActivityMessage

def what_am_i_doing(request):
    now = datetime.now()
    hour = now.hour
    weekday = now.weekday()  # 0 = Monday, 6 = Sunday
    date_str = now.strftime('%m-%d')  # For comparing with holidays

    # Log the time_slot and weekday to check their values
    print(f"Current time: {hour}, Weekday: {weekday}, Date: {date_str}")

    # Check if today is a holiday!
    holiday_message = ActivityMessage.objects.filter(holiday=date_str).first()
    if holiday_message:
        return JsonResponse({"message": holiday_message.message})

    # Determine if it's a weekday or weekend
    is_weekend = True if weekday >= 5 else False  # 5 = Saturday, 6 = Sunday (weekend)

    print(f"Is weekend: {is_weekend}")

    # Get the appropriate messages for the current time slot
    time_slot = None
    if 5 <= hour < 8:
        time_slot = 'early_morning'
    elif 8 <= hour < 12:
        time_slot = 'morning'
    elif 12 <= hour < 13:
        time_slot = 'lunch'
    elif 13 <= hour < 17:
        time_slot = 'afternoon'
    elif 17 <= hour < 20:
        time_slot = 'evening'
    elif 20 <= hour < 23:
        time_slot = 'night'
    else:  # 23:00–4:59
        time_slot = 'late_night'

    print(f"Determined time_slot: {time_slot}")

    # Fetch the appropriate messages for the time slot and weekend/weekday
    messages = ActivityMessage.objects.filter(time_slot=time_slot, is_weekend=is_weekend)
    if messages.exists():
        message = random.choice(messages).message
    else:
        message = "Doing something random..."

    return JsonResponse({"message": message})
