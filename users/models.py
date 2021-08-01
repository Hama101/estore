from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User , blank=True ,on_delete=models.CASCADE)
    name = models.CharField(max_length=200 ,blank=True,null=True)
    avatar = models.ImageField(blank=True , null=True , upload_to='Profile/')
    cover = models.ImageField(blank=True , null=True , upload_to='Profile/')
    is_buyer = models.BooleanField(default=False)
    products = models.ManyToManyField(Product)
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