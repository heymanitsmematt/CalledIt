from django.contrib import admin
from app.models import UserProfile, Sport, Event, Party, Prediction

admin.site.register(UserProfile)
admin.site.register(Sport)
admin.site.register(Event)
admin.site.register(Party)
admin.site.register(Prediction)

