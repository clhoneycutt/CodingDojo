from django.db import models
from ..users.models import User

class messageManager(models.Manager):

    def validateMsg(self, messageInfo):

        errors = []

        if len(messageInfo['post_message']) < 1:
            errors.append("Message cannot be blank")

        return errors
    
    def addMessage(self, messageInfo):
        user = User.objects.get(id=messageInfo['userid'])
        message = messageInfo['post_message']
        newMessage = self.create(
            user = user,
            message = message
            )
        newMessage.save()
        return True
    
    def displayMessages(self):
        allMessages = self.all().values()
        displayMessages = []
        for message in allMessages:
            
            displayMessages.append({
                'message': message,
                'user': User.objects.filter(id=allMessages[0]['user_id']).values()
            })
        return displayMessages



class Message(models.Model):
    user = models.ForeignKey(User, related_name="messages")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = messageManager()

class Comment(models.Model):
    message = models.ForeignKey(Message, related_name="comments")
    user = models.ForeignKey(User, related_name="comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
