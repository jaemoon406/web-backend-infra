from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)

    class Meta:
        db_table = 'posts'
