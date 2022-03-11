from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# slugify is used to put _ instaed of spaces so that it can further be used in urls
# Create your models here.
import misaka
# misaka puts link or marked text but you have to install it first
from django.contrib.auth import get_user_model
 # returns user model currently active in this project
User= get_user_model()
# object creation
from django import template
register = template.Library()
        # explanation not in lecture 181
class Group(models.Model):
    name=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(allow_unicode=True,unique=True)
    description=models.TextField(blank=True,default='write somethinng')
    description_html=models.TextField(editable=False,default='',blank=True)
    members=models.ManyToManyField(User,through='GroupMember')
    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html=misaka.html(self.description)
        super().save(*args,**kwargs)
    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})
    class Meta:
        ordering=['name']
class GroupMember(models.Model):
    group=models.ForeignKey(Group,related_name='memberships',on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name='user_groups',on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    class Meta:
        unique_together=('group','user')
        # explanation not in lecture 181
