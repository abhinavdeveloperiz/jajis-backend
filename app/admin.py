from django.contrib import admin
from .models import BannerImage, Saloon, Cosmetics,FoodMenu,Courses,Category,Product,ProductVariant,Cart,CartItem,Address,Order,OrderItem,PaymentTransaction



admin.site.register(BannerImage)
admin.site.register(Saloon)
admin.site.register(Cosmetics)
admin.site.register(FoodMenu)
admin.site.register(Courses)

# e commerse 
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductVariant)
admin.site.register(Cart)
admin.site.register(CartItem)


admin.site.register(Address)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(PaymentTransaction)




