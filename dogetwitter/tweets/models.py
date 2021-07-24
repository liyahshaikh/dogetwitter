from django.db import models

# Create your models here.
class Tweet(models.Model):
    #id = models.AutoField(primary_key=True) Its automatically present to distinguish the individual tweets.
    content=models.TextField(blank =True, null=True) #To be checked, if tweets with no content and Image can be tweeted.
    image=models.FileField(upload_to="image/", blank=True, null=True) #blank: Not required in Django, null: Not required in the database too.
    
