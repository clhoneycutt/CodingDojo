from django.db import models
from ..users.models import User

class messageManager(models.Manager):

    def validateMsg(self, messageInfo):

        errors = []

        if len(messageInfo['post_message']) < 1:
            errors.append("Message cannot be blank")

        return errors
    
    def addMessage(self, messageInfo, userid):
        userid = User.objects.get(id=userid)
        newMessage = self.create(
            userid = userid,
            message = messageInfo['post_message']
            )
        return
    
    def displayMessages(self, userid):
        allMessages = self.filter(userid=userid)
        return allMessages



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
