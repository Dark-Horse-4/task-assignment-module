from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Task , UserImage


class ProfileInline(admin.StackedInline):
    model = UserImage
    can_delete = False
    verbose_name_plural = 'UserImage'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff','userimage')
    list_select_related = ('userimage', )

    def get_image(self, instance):
        return instance.userimage.image.url
    get_image.short_description = 'image'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Task)