from django.contrib import admin

from .models import User, Role

 

class UserAdmin(admin.ModelAdmin):

    list_display = ("user_name", "email", "role") 

 

admin.site.register(User, UserAdmin)

 

class RoleAdmin(admin.ModelAdmin):

    pass  # Add any customizations for the Role admin here

 

admin.site.register(Role, RoleAdmin)
