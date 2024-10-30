from django.db import models
from django.contrib.auth.models import User
from item.models import Item

# Create your models here.
class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name="conversations", on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name="conversations")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "conversation"
        verbose_name_plural = "conversations"
        ordering = ("-modified_at",)

    def __str__(self):
        return self.name
    
    
class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name="messages", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "conversation message"
        verbose_name_plural = "conversation messages"
        ordering = ("created_at",)
        
    def __str__(self):
        return self.name


