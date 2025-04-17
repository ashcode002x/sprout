from django.db import models
import uuid
from multiselectfield import MultiSelectField

# Create your models here.
class Meeting(models.Model):
    "Meeting model to store meeting details and permissions."
    
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False,primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(null=True, blank=True)
    
    # Permission choices as class constants for better organization
    PERMISSION_CHOICES = [
        ('UserScreenShare', 'Screen Share'),
        ('UserVideo', 'Video'),
        ('UserAudio', 'Audio'),
        ('UserChat', 'Chat'),
        ('UserRaiseHand', 'Raise Hand'),
        ('UserWhiteboard', 'Whiteboard'),
        ('UserPoll', 'Poll'),
        ('UserBreakoutRoom', 'Breakout Room'),
    ]
    
    # Multiple choice permissions field
    permissions = MultiSelectField(
        choices=PERMISSION_CHOICES,
        max_choices=8,
        max_length=150,
        blank=True
    )
    
    # host=models.ForeignKey()
    
    # Meeting type choices
    MEETING_TYPE_CHOICES = [
        ('Public', 'Public'),
        ('Private', 'Private'),
        # ('Protected', 'Protected'),
    ]
    
    meeting_type = models.CharField(
        max_length=10,
        choices=MEETING_TYPE_CHOICES
    )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Meeting"
        verbose_name_plural = "Meetings"