from django.shortcuts import render,redirect
# import loginrequired
from django.contrib.auth.decorators import login_required
from .forms import MeetingForm
from .models import Meeting
from django.http import HttpResponseRedirect
import os
# Create your views here.

def home(request):
    "sending the meeting form to the home page"
    form = MeetingForm()
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            #  retreive the meeting obj and redirect to the meeting page
            meeting_id = form.instance.id
            return redirect('meeting:meeting', meeting_id=meeting_id)
    else:
        form = MeetingForm()
    context = {'form': form}

    return render(request, 'home.html', context)

def meeting(request, meeting_id):
    "displaying the meeting page"
    #  retreive the meeting obj and display it
    meeting = Meeting.objects.get(id=meeting_id)
    context = {'meeting': meeting}
    return render(request, 'meeting.html', context)


def join_meeting(request, meeting_id):
    """Render the join meeting page with video conference interface"""
    meeting = Meeting.objects.get(id=meeting_id)
    context = {'meeting': meeting,'socket_server_url': os.environ.get('SOCKET_SERVER_URL', 'http://127.0.0.1:5000')}
    return render(request, 'join-meeting.html', context)