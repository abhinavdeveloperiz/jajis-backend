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
    image1=models.ImageField(upload_to='saloon_images/',blank=True,null=True)
    image2=models.ImageField(upload_to='saloon_images/',blank=True,null=True)
    image3=models.ImageField(upload_to='saloon_images/',blank=True,null=True)
    image4=models.ImageField(upload_to='saloon_images/',blank=True,null=True)
    image5=models.ImageField(upload_to='saloon_images/',blank=True,null=True)
    image6=models.ImageField(upload_to='saloon_images/',blank=True,null=True)
    google_map_url=models.CharField(max_length=1000,null=True,blank=True)
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Saloon"
        verbose_name_plural = "Saloon"
    

class FoodMenu(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='food_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Food Menu"
        verbose_name_plural = "Food Menu"

    
class Cosmetics(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='cosmetics_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Cosmetic"
        verbose_name_plural = "Cosmetics"


class Courses(models.Model):

    image=models.ImageField(upload_to='courses/')
    course=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    description=models.TextField()

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

