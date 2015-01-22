from django.contrib import admin
from app.models import User, Sport, Event, Party, Prediction

admin.site.register(User)
admin.site.register(Sport)
admin.site.register(Event)
admin.site.register(Party)
admin.site.register(Prediction)

