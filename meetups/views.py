from django.shortcuts import render, redirect
from .models import Meetups, Participants

from .forms import RegistrationForm
# Create your views here.

def index(request):

    meetups = Meetups.objects.all()
    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):
    
    try:
        selected_meetup = Meetups.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
          
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participants.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration', meetup_slug=meetup_slug)

        return render(request, 'meetups/meetup-details.html', {
                'meetup_found': True,
                'meetup': selected_meetup,
                'form': registration_form 
                # 'meetup_title': selected_meetup.title,
                # 'meetup_description': selected_meetup.description
            })

    except Exception as exc:
        
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False,
            'exc': exc
        })


    
def confirm_registration(request, meetup_slug):
    meetup = Meetups.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html', {
        'organizer_email': meetup,
    })