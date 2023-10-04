from django.db import models

# Create your models here.

class Moviedata(models.Model):

    def __str__(self):
        return self.name
    
    name=models.CharField(max_length=200)
    duration=models.FloatField()
    ratings=models.CharField(max_length=20,default='no rating')
    typ=models.CharField(max_length=200,default='action')
    # typ gives the information of only those movies  which type is action.
    image=models.ImageField(upload_to='Images/',default='Images/None/Noimg.jpg')
