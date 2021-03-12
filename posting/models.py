from django.db import models

class Post(models.Model):
    user       = models.ForeignKey('user.User', on_delete = models.CASCADE)
    image_url  = models.CharField(max_length=2000)
    contents   = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table: 'posts'
