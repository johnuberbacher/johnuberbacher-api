from django.db import models

class ActivityMessage(models.Model):
    time_slot = models.CharField(max_length=50)  # e.g., 'morning', 'afternoon', etc.
    is_weekend = models.BooleanField()  # Boolean field to indicate if the message is for weekend
    holiday = models.CharField(max_length=50, null=True, blank=True)  # Optional holiday name
    message = models.TextField()  # The actual message

    def __str__(self):
        return f"{self.time_slot} - {self.message}"
