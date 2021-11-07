from django.contrib import admin
from .models import Contact, Teacher, Branch


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone_number',
        'email',
        'message',
        'created_date'
    )
    list_filter = ('name',)
    search_fields =('name__startswith',)


class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'phone_teacher',
        'email_teacher',
        'speciality',
        'updateDate',
        'createdDate'

    )
    list_filter = ('first_name',)
    search_fields =('first_name__startswith',)


# Register your models here.
admin.site.register(Contact, ContactAdmin)


admin.site.register(Teacher, TeacherAdmin)

admin.site.register(Branch)
