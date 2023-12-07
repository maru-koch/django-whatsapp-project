from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
import uuid

# CUSTOM USER Manager
class CustomUserManager(BaseUserManager):
    pass

# CUSTOM USER
class CustomUser(AbstractUser):
    id = models.UUIDField(default = uuid.uuid4, primary_key=True, unique=True)
    phone_number = models.Charfield('phone_number', max_length=255, unique=True, blank=False, null=False)
    first_name = models.CharField('first_name')

# MESSAGE MODEL
class MessageModel(models.Model):
    """Message model. Fields include id, body, sender, receiver, and timestamp. """
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, null=False, editable=False)
    body = models.TextField('body', editable=False)
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="receiver")
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="sender")
    timestamp = models.DateTimeField('timestamp', auto_add_now=True)
    is_read = models.BooleanField(default= False)
    
    class Meta:
        app_name="core"
        verbose_name = "message"
        verbose_name_plural = "messages"
        ordering="-timestamp"

    def __str__(self):
        return self.body


