from django.contrib import admin
from .models import Student, Group, Club

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'curator')
    search_fields = ('name', 'curator')

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'group_name')
    list_filter = ('group', 'clubs')
    search_fields = ('first_name', 'last_name')
    filter_horizontal = ('clubs',)

    def group_name(self, obj):
        return obj.group.name if obj.group else '-'
    group_name.short_description = 'Группа'
