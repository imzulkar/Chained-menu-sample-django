from django.contrib import admin
from user import models, forms
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class AdminUser(UserAdmin):
    ordering = ('-date_joined',)
    search_fields = ('username', 'email', 'full_name', 'phone_number')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'gender')
    list_display = ('username', 'email', 'full_name', 'country', 'date_joined', 'is_active')
    fieldsets = (
        ('Login Info', {'fields': ('username', 'email', 'password')}),
        ('User Information',
         {'fields': (
             'full_name', 'gender', 'profile_pic', 'birth_date', 'address_one', 'address_two', 'city', 'zipcode',
             'country', 'phone_number',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'full_name', 'password1', 'password2'),
        }),
    )


admin.site.register(models.User, AdminUser)

# class YourModelAdmin(admin.ModelAdmin):
#     form = models.ProjectForm
#
#     # list_display = ['your fields',]
#     class Media:
#         js = ("/static/user/admin_config.js",)


# admin.site.register(models.Project, YourModelAdmin)
admin.site.register(models.Phase)
admin.site.register(models.ProjectPhase)


class WarehouseAdmin(admin.ModelAdmin):
    form = forms.WarehouseForm

    class Media:
        js = (
            "/static/user/admin_config.js",
        )


# class WarehouseAdmin(admin.ModelAdmin):
#     form = forms.WarehouseForm


admin.site.register(models.Warehouse, WarehouseAdmin)
admin.site.register(models.Kelurahan)
admin.site.register(models.Kecamatan)
admin.site.register(models.Kabupaten)
admin.site.register(models.Provinsi)
