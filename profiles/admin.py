from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from profiles.models import Profile
from django import forms

# Register your models here.


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name",
                  "email", "password1", "password2")

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not first_name:
            raise forms.ValidationError("First name is required.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if not last_name:
            raise forms.ValidationError("Last name is required.")
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("Email is required.")
        return email


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'
    fields = ("phone",)


class ProfileAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ("username", "get_name", "get_email", "get_phone")

    def get_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    get_name.short_description = "Full Name"

    def get_email(self, obj):
        return obj.email
    get_email.short_description = "Email"

    def get_phone(self, obj):
        return obj.profile.phone if hasattr(obj, "profile") else None
    get_phone.short_description = "Phone Number"

    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "first_name", "last_name", "email", "password1", "password2"),
        }),
    )


admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
admin.site.unregister(Group)
