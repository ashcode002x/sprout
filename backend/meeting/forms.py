from django import forms
from django.forms import ModelForm, DateTimeInput
from .models import Meeting

class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = ['name', 'description', 'start_time', 'end_time', 'permissions', 'meeting_type']
        exclude = ['meeting_id']  # Auto-generated field, no need for user input
        
        widgets = {
            'start_time': DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'permissions': forms.CheckboxSelectMultiple(),
        }
        
        help_texts = {
            'name': 'Enter a unique name for your meeting',
            'start_time': 'Select the meeting start date and time',
            'end_time': 'Select the meeting end date and time',
            'permissions': 'Select the features available to participants (multiple options allowed)',
            'meeting_type': 'Public meetings can be joined by anyone with the link',
        }
        
    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        
        if start_time and end_time and start_time >= end_time:
            raise forms.ValidationError("End time must be after start time")
            
        return cleaned_data