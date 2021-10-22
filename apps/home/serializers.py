from rest_framework import serializers
from .models import EventList

class EventSerilizer(serializers.ModelSerializer):
  class Meta:
    model = EventList
    fields = ["eventname", "eventdate", "predtime", "emerge"]
    read_only_fields = ('id',)