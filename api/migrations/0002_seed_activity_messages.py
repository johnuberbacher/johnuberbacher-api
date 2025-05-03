from django.db import migrations

# Predefined messages for seeding
activity_messages = [
    { "time_slot": "early_morning", "is_weekend": False, "message": "Still half asleep, but making it work." },
    { "time_slot": "early_morning", "is_weekend": False, "message": "Good morning, world... is it too early for breakfast?" },
    { "time_slot": "early_morning", "is_weekend": False, "message": "I swear I just blinked, and it's time to get up!" },
    { "time_slot": "early_morning", "is_weekend": False, "message": "Out of bed, into the grind... but mostly still dreaming." },
    { "time_slot": "early_morning", "is_weekend": False, "message": "Coffee in hand, pretending to be a functional adult." },
    { "time_slot": "early_morning", "is_weekend": True, "message": "The world is quiet, and so is my brain." },
    { "time_slot": "early_morning", "is_weekend": True, "message": "Early mornings, endless coffee." },
    { "time_slot": "early_morning", "is_weekend": True, "message": "Just woke up... or maybe I didn’t sleep at all." },
    { "time_slot": "early_morning", "is_weekend": True, "message": "The sun's up, but so are my blankets." },
    { "time_slot": "early_morning", "is_weekend": True, "message": "Another morning where I question why the bed isn't a permanent home." },
    # Morning
    { "time_slot": "morning", "is_weekend": False, "message": "Mornings are for coffee and to-do lists." },
    { "time_slot": "morning", "is_weekend": False, "message": "The struggle of making a list... and then forgetting it." },
    { "time_slot": "morning", "is_weekend": False, "message": "Rise and grind... but mostly grind the coffee." },
    { "time_slot": "morning", "is_weekend": False, "message": "First step: Get out of bed. Step two: Hope it’s Friday." },
    { "time_slot": "morning", "is_weekend": False, "message": "Time to pretend I’m organized for the day." },
    { "time_slot": "morning", "is_weekend": True, "message": "Rise and shine... or at least try to." },
    { "time_slot": "morning", "is_weekend": True, "message": "Starting the day slow—coffee in hand." },
    { "time_slot": "morning", "is_weekend": True, "message": "Getting into the groove, one task at a time." },
    { "time_slot": "morning", "is_weekend": True, "message": "Mornings are for adventures... or just staying in pajamas." },
    { "time_slot": "morning", "is_weekend": True, "message": "The early bird catches the worm... or at least the coffee." },
    # Lunch
    { "time_slot": "lunch", "is_weekend": False, "message": "Midday break: time for food and a little rest." },
    { "time_slot": "lunch", "is_weekend": False, "message": "Lunch: where productivity goes to take a nap." },
    { "time_slot": "lunch", "is_weekend": False, "message": "Time to refuel! I mean, I *was* working, right?" },
    { "time_slot": "lunch", "is_weekend": False, "message": "Lunch break: because we all deserve a moment to stare into space." },
    { "time_slot": "lunch", "is_weekend": False, "message": "Munching away while pretending not to check emails." },
    { "time_slot": "lunch", "is_weekend": True, "message": "Lunchtime! Fueling up for the second half." },
    { "time_slot": "lunch", "is_weekend": True, "message": "Taking a breather before the afternoon rush." },
    { "time_slot": "lunch", "is_weekend": True, "message": "Sitting down to eat, but my mind’s still racing." },
    { "time_slot": "lunch", "is_weekend": True, "message": "Eating like I’m on a road trip. I’ve got snacks for days." },
    { "time_slot": "lunch", "is_weekend": True, "message": "Lunchtime, or 'try to finish a sandwich without getting crumbs everywhere.'" },
    # Afternoon
    { "time_slot": "afternoon", "is_weekend": False, "message": "Pushing through the afternoon slump." },
    { "time_slot": "afternoon", "is_weekend": False, "message": "The afternoon is when coffee is more of a survival tool." },
    { "time_slot": "afternoon", "is_weekend": False, "message": "Is it too early to count down the minutes till the end of the day?" },
    { "time_slot": "afternoon", "is_weekend": False, "message": "Trying to look busy while daydreaming of dinner." },
    { "time_slot": "afternoon", "is_weekend": False, "message": "Just trying to stay awake and pretend I'm on top of things." },
    { "time_slot": "afternoon", "is_weekend": True, "message": "Afternoon energy: half gone, half still going." },
    { "time_slot": "afternoon", "is_weekend": True, "message": "Trying to finish strong before the end of the day." },
    { "time_slot": "afternoon", "is_weekend": True, "message": "Powering through my to-do list, one task at a time." },
    { "time_slot": "afternoon", "is_weekend": True, "message": "That post-hike glow is real, but so is the need for snacks." },
    { "time_slot": "afternoon", "is_weekend": True, "message": "Afternoon plans: Find snacks and take a nap... maybe in that order." },
    # Evening
    { "time_slot": "evening", "is_weekend": False, "message": "Evening vibes: winding down or just getting started?" },
    { "time_slot": "evening", "is_weekend": False, "message": "Dinner time! A.k.a. the best time of the day." },
    { "time_slot": "evening", "is_weekend": False, "message": "Another evening, another attempt at productivity... but first, snacks." },
    { "time_slot": "evening", "is_weekend": False, "message": "The workday is over... now it’s time to pretend to relax." },
    { "time_slot": "evening", "is_weekend": False, "message": "Evenings are for unwinding, unless you're working late... again." },
    { "time_slot": "evening", "is_weekend": True, "message": "Time for dinner and a little relaxation." },
    { "time_slot": "evening", "is_weekend": True, "message": "Finally, some time to breathe after the workday." },
    { "time_slot": "evening", "is_weekend": True, "message": "Chasing sunset vibes and evening calm." },
    { "time_slot": "evening", "is_weekend": True, "message": "Dinner, good company, and lots of silly stories." },
    { "time_slot": "evening", "is_weekend": True, "message": "Evening plans: Relax, maybe get some sleep... and by sleep, I mean more coffee." },
    # Night
    { "time_slot": "night", "is_weekend": False, "message": "Night mode: catching up on shows or books." },
    { "time_slot": "night", "is_weekend": False, "message": "When the night starts, and the procrastination kicks in." },
    { "time_slot": "night", "is_weekend": False, "message": "Ready to binge-watch some shows... or accidentally scroll the internet forever." },
    { "time_slot": "night", "is_weekend": False, "message": "The day is over, and the couch is calling my name." },
    { "time_slot": "night", "is_weekend": False, "message": "Nighttime: when all of life’s decisions seem a little more... questionable." },
    { "time_slot": "night", "is_weekend": True, "message": "Settling in for a quiet evening after a busy day." },
    { "time_slot": "night", "is_weekend": True, "message": "A few hours left to enjoy the night." },
    { "time_slot": "night", "is_weekend": True, "message": "Nighttime, when productivity fades and relaxation begins." },
    { "time_slot": "night", "is_weekend": True, "message": "The best part of the night? No alarms tomorrow." },
    { "time_slot": "night", "is_weekend": True, "message": "Night mode: Dim lights, good books, and no agenda." },
    # Late Night
    { "time_slot": "late_night", "is_weekend": False, "message": "Late-night thoughts: should I sleep yet?" },
    { "time_slot": "late_night", "is_weekend": False, "message": "The moon is up, but so is my need to keep working... or not." },
    { "time_slot": "late_night", "is_weekend": False, "message": "Late night snacks: The only thing keeping me awake." },
    { "time_slot": "late_night", "is_weekend": False, "message": "Is it bedtime yet, or just one more episode?" },
    { "time_slot": "late_night", "is_weekend": False, "message": "Late-night grind: Is anyone else still awake? No? Just me?" },
    { "time_slot": "late_night", "is_weekend": True, "message": "Everything’s quiet... maybe too quiet." },
    { "time_slot": "late_night", "is_weekend": True, "message": "Late-night grind: pushing through the hours." },
    { "time_slot": "late_night", "is_weekend": True, "message": "Winding down or just procrastinating bedtime?" },
    { "time_slot": "late_night", "is_weekend": True, "message": "Late-night thoughts: Why is it so hard to turn off Netflix?" },
    { "time_slot": "late_night", "is_weekend": True, "message": "It's so quiet... but also so much fun to be awake!" }
]

def seed_activity_messages(apps, schema_editor):
    # Get the model for ActivityMessage
    ActivityMessage = apps.get_model('api', 'ActivityMessage')

    # Insert each activity message into the database
    for msg in activity_messages:
        ActivityMessage.objects.create(**msg)

def reverse_seed_activity_messages(apps, schema_editor):
    # Reverse function to delete the seeded data (if necessary)
    ActivityMessage = apps.get_model('api', 'ActivityMessage')
    for msg in activity_messages:
        ActivityMessage.objects.filter(holiday=msg['holiday'], time_slot=msg.get('time_slot')).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_activity_messages, reverse_code=reverse_seed_activity_messages),
    ]
