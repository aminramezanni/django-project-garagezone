from django.db import models

# Create your models here.


class Team(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    designation = models.CharField(max_length=225)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    instagram_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'
    


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=200)
    site_url = models.URLField(max_length=200)
    address = models.CharField(max_length=250)
    phone_number = models.IntegerField(null=True,blank=True)
    email = models.EmailField(max_length=250,null=True,blank=True)
    fax = models.CharField(max_length=200,null=True,blank=True)
    copyright_text = models.TextField()

    def __str__(self):
        return self.site_name
