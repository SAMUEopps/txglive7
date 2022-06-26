from django.db import models
from .utils import generate_ref_code
# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(blank=True)
	code = models.CharField(max_length=12, blank=True)
	recomended_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='ref_by')
	updated = models.DateTimeField(auto_now=True)
	craeted = models.DateTimeField(auto_now_add=True)

	def __str__ (self):
		return f"{self.user.username}-{self.code}"

	def get_recomended_profiles(self):
		qs = Profile.objects.all()
		#my_recs = [p for p in qs.recomended_by == self.user]

		my_recs = []
		for profile in qs:
			if profile.recomended_by == self.user:
				my_recs.append(profile)
		return my_recs
	

	def save(self, *args, **kwargs):
		if self.code == "":
			code = generate_ref_code()
			self.code = code
		super().save(*args,**kwargs)


class Reg_fee(models.Model):
	username = models.CharField(max_length=300, unique=True)
	mpesa_code = models.CharField(max_length=300, unique=True)
	full_names = models.CharField(max_length=300, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	

#class Deposit(models.Model):
#	username = models.CharField(max_length=300, unique=True)
#	mpesa_code = models.CharField(max_length=300, unique=True)
#	full_name = models.CharField(max_length=300, unique=True)
#	created_at = models.DateTimeField(auto_now_add=True)    
		