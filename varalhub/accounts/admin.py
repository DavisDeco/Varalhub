from django.contrib import admin
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# from .models import GuestEmail, EmailActivation
from .forms import UserAdminChangeForm,UserAdminCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

#####################################
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    list_display = ('email','username','active','staff', 'admin')
    list_filter = ('admin','staff','active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username',)}),
        ('Permissions', {'fields': ('admin','staff','active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','username','password1', 'password2')}
        ),
    )
    search_fields = ('email','username')
    ordering = ('email',)
    filter_horizontal = ()


# Register the userAdmin
admin.site.register(User, UserAdmin)



# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
