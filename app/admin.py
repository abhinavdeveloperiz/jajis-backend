from django.contrib import admin
from .models import BannerImage, Saloon, Cosmetics,FoodMenu,Courses,Category,Product,ProductVariant



admin.site.register(BannerImage)
admin.site.register(Saloon)
admin.site.register(Cosmetics)
admin.site.register(FoodMenu)
admin.site.register(Courses)

# e commerse 
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductVariant)




