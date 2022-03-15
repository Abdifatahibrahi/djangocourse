from django.contrib import admin
from .models import Meetups, Location, Participants

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'image','location' )
    list_filter = ('location', 'date' )
    prepopulated_fields = {'slug': ('title',)}

class LocationAdmin(admin.ModelAdmin):
        list_display = ('name', 'address',)

class ParticipantsAdmin(admin.ModelAdmin):
        list_display = ('email',)


admin.site.register(Meetups, MeetupAdmin)

admin.site.register(Location, LocationAdmin)

admin.site.register(Participants, ParticipantsAdmin)

