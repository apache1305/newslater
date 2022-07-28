from django.contrib import admin
from .models import *
# Register your models here.
# class UserAdmin(User):
#     pass
# class CategoryAdmin(User):
#     pass 
# class NewsletterAdmin(User):
#     pass 
# class SubscriptionAdmin(User):
#     pass 
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Newsletter)
admin.site.register(Subscription)