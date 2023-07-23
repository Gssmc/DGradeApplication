from django.db import models
from django.conf import settings
# Create your models here.



'''
class Complain(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title=models.CharField(max_length=100,null=False)
    desc=models.TextField(max_length=300,null=False)

    def __str__(self):
        return self.title+" -- by "+self.author.username

    #calling image compression function before saving the data
    def save(self, *args, **kwargs):
        super(Complain,self).save(*args, **kwargs)
'''
class Notification(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title=models.CharField(max_length=100,null=False)
    desc=models.TextField(max_length=300,null=False)

    def __str__(self):
        return self.title

    #calling image compression function before saving the data
    def save(self, *args, **kwargs):
        super(Notification,self).save(*args, **kwargs)