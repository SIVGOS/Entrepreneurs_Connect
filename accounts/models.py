from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class entrepreneur(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	photo = models.ImageField(upload_to='photos', blank=True)
	intro = models.CharField(max_length=300, blank=True)
	industry = models.CharField(max_length = 50, blank=True)
	city = models.CharField(max_length=100, blank=True)
	state = models.CharField(max_length=100, blank=True)
	country = models.CharField(max_length=100, blank=True)
	about = models.TextField(blank=True)
	linkedin_url = models.URLField(max_length=200, blank=True)
	facebook_url = models.URLField(max_length=200, blank=True)
	instagram_url = models.URLField(max_length=200, blank=True)
	business_pic1 = models.ImageField(upload_to='bpics', blank=True)
	business_pic2 = models.ImageField(upload_to='bpics', blank=True)
	business_pic3 = models.ImageField(upload_to='bpics', blank=True)
	business_pic4 = models.ImageField(upload_to='bpics', blank=True)
	business_pic5 = models.ImageField(upload_to='bpics', blank=True)


