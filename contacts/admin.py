from django.contrib import admin

from contacts.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'first_name', 'last_name', 'email', 'phone', 'user')  
    search_fields = ('name', 'email', 'user__username')  
    list_filter = ('user',)
    exclude = ('user',)


admin.site.register(Contact, ContactAdmin)