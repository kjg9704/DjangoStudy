from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    postname = models.CharField(max_length=50)
    contents = models.TextField()

    def __str__(self):
        return self.postname
