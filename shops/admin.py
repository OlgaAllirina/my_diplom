from django.contrib import admin
from models import Shop, User

# Register your models here.

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

