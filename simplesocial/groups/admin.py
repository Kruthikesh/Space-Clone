from django.contrib import admin
from django.db import models

from groups.models import Group,GroupMember
# Register your models here.
class GroupMemberInline(admin.TabularInline):
    model=GroupMember

admin.site.register(Group)
admin.site.register(GroupMember)
