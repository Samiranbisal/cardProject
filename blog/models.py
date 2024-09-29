from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')  # 'upload_to' defines where the image will be saved
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
