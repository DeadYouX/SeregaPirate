from django.db import models
from ForumProfile.models import Profile

class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100)

    def message_count(self):
        return self.messages.count()
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Чат"
        verbose_name_plural="Чаты"

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"\'{self.chat.name}\': {self.content}"

    class Meta:
        verbose_name="Сообщение"
        verbose_name_plural="Сообщения"