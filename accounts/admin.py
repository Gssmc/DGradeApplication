from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
 

from .models import MyUser
from .forms import UserCreationForm,UserChangeForm

# admin site customization start
admin.site.site_title = "D-grade"
admin.site.site_header = "D-grade Admin Login"

#admin site customiztion end

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_admin','username','institution','account_type','contact','account_type','address')
    list_filter = ('is_admin',)
    fieldsets = (
        ('information', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('institution','username','address','contact','account_type')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'institution','username', 'account_type','password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)