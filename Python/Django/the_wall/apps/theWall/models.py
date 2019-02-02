from django.db import models
from ..users.models import User

class messageManager(models.Manager):

    def validateMsg(self, messageInfo):

        errors = []

        if len(messageInfo['post_message']) < 1:
            errors.append("Message cannot be blank")

        return errors
    
    def addMessage(self, messageInfo):
        newMessage = self.create(
            user = User.objects.get(id=messageInfo['userid']),
            message = messageInfo['post_message']
            )
        newMessage.save()
        return

class commentManager(models.Manager):

    def validateComment(self, commentInfo):

        errors = []

        if len(commentInfo['post_comment']) < 1:
            errors.append("Comment cannot be blank")

        return errors

    def addComment(self, commentInfo):
        newComment = self.create(
            message = Message.objects.get(id=commentInfo['messageid']),
            user = User.objects.get(id=commentInfo['userid']),
            comment = commentInfo['post_comment']
        )
        return



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
    objects = commentManager()
