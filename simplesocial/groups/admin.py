from django.contrib import admin
from . import models
# Register your models here.

class GroupMemberInline(admin.TabularInline): 
	model = models.GroupMember

'''
TabularInline allows us to utilize the admin interface and our Django website 
with ability to edit models on the same page as the parent model
'''

admin.site.register(models.Group)