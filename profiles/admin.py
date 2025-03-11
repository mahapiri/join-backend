from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from profiles.models import Profile

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class ProfileAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'first_name', 'last_name', 'email', 'get_phone')

    def get_phone(self, obj):
        return obj.profile.phone if hasattr(obj, 'profile') else None
    get_phone.short_description = 'Phone Number'

admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
admin.site.unregister(Group)