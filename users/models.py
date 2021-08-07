from django.db import models
from django.contrib.auth.models import User
from products.models import Product

from ckeditor.fields import RichTextField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User , blank=True ,on_delete=models.CASCADE)
    name = models.CharField(max_length=200 ,blank=True,null=True , unique=True)
    
    avatar = models.ImageField(blank=True , null=True , upload_to='Profile/')
    cover = models.ImageField(blank=True , null=True , upload_to='Profile/')
    
    is_buyer = models.BooleanField(default=False)
    products = models.ManyToManyField(Product ,blank=True , null=True)
    
    type = models.CharField(max_length=30 , blank=True ,null=True )
    address = models.CharField(max_length=30 , blank=True ,null=True )
    employees_number = models.IntegerField(blank=True , null=True)
    
    web_site = models.CharField(max_length=5080 , blank=True , null=True)
    
    about_me = RichTextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField( null=False, blank = False)
    secondPhoneNumber = models.IntegerField(null = True, blank = True)
    postcode = models.IntegerField(null = True, blank = True)
    
    created_at = models.DateTimeField(auto_now=True , blank=True , null=True)
    
    
    
    @property
    def avatar_url(self):
        if self.avatar :
            return self.avatar.url
        else:
            return f"https://www.kindpng.com/picc/m/20-208238_small-business-white-new-business-icon-hd-png.png"
    
    @property
    def cover_url(self):
        if self.cover :
            return self.cover.url
        else:
            return f"https://www.americancityandcounty.com/files/2020/06/sean-pollock-PhYq704ffdA-unsplash-2-1024x512.jpg"
    
    def __str__(self):
        return f"{self.name}"