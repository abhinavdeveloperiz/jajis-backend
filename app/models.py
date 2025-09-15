from django.db import models

class BannerVideo(models.Model):
    
    video = models.FileField(upload_to='page_videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Video {self.id}"


class Saloon(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='saloon_images/')
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    

    
class Cosmetics(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='cosmetics_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title