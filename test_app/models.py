# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField, Model
from django_mysql.models import ListCharField

class UserDetails(models.Model):
	user_acc = models.OneToOneField(User,on_delete=models.CASCADE)
	note = ListCharField(default=None,base_field=CharField(max_length=100),size=50,max_length=6000)
	class Meta:
		db_table = "user_details"
