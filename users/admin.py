from django.contrib import admin
from content_app.models import Content
from .models import User

admin.site.register(Content)


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    list_filter = ('role', 'is_active', 'is_staff')


admin.site.register(User, UserAdmin)