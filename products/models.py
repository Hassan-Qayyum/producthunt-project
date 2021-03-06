from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE) #It will save user object not only id
    title = models.CharField(max_length = 255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to = 'image/')
    icon = models.ImageField(upload_to = 'image/')
    votes_total = models.IntegerField(default = 1)



    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime(' %b %e %Y')

    def summary(self):
        return self.body[:100]
