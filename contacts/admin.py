from django.contrib import admin

from contacts.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')
    list_filter = ('email',)


admin.site.register(Contact, ContactAdmin)