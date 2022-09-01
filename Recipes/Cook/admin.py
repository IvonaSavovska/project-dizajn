from django.contrib import admin
from .models import Admin, Login, MealPlanner, ContactCenter
# Register your models here.

class AdminAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Admin,AdminAdmin)

class LoginAdmin(admin.ModelAdmin):
    pass

admin.site.register(Login,LoginAdmin)

class MealPlannerAdmin(admin.ModelAdmin):
    pass

admin.site.register(MealPlanner,MealPlannerAdmin)

class ContactCenterAdmin(admin.ModelAdmin):
    pass

admin.site.register(ContactCenter, ContactCenterAdmin)

