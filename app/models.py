from django.db import models
from django.contrib.auth.models import User


class BannerImage(models.Model):
    
    image = models.ImageField(upload_to="banner_image/",null=True,blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}"


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



# -------------e-commerse--------------------------
class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")

    title = models.CharField(max_length=255)
    description = models.TextField()
    brand = models.CharField(max_length=100, blank=True, null=True,default="jajis")

    image1 = models.ImageField(upload_to='product_images/')
    image2 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='product_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)

    quantity_label = models.CharField(max_length=50)

    mrp = models.DecimalField(max_digits=10, decimal_places=2)      
    price = models.DecimalField(max_digits=10, decimal_places=2)    

    stock = models.PositiveIntegerField(default=0)
    sku = models.CharField(max_length=100, blank=True, null=True, unique=True)

    def __str__(self):
        return f"{self.product.title} - {self.quantity_label}"
    




class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Cart"
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'variant')

    def __str__(self):
        return f"{self.variant} x {self.quantity}"