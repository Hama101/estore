from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True , unique=True)
    image = models.ImageField(blank=True,null=True , upload_to='Category/')
    
    def __str__(self):
        return f"{self.title}"
    
    @property
    def img_url(self):
        if self.image:
            return self.image.url
        else:
            return f"https://i.ytimg.com/vi/2QvOxa_7wEw/maxresdefault.jpg"


class Mark(models.Model):
    name = models.CharField(max_length=200 , blank=True ,null=True,unique=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE, blank=True ,null=True)
    
    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    cover = models.ImageField(blank=True,null=True , upload_to='Products/')
    price = models.FloatField(null=True,blank=True)
    category = models.ForeignKey(Category , blank=True , null=True , on_delete=models.CASCADE)
    mark = models.ForeignKey(Mark , null=True, blank=True,on_delete=models.CASCADE)
    #ect...
    img1 = models.ImageField(blank=True,null=True , upload_to='Products/')
    img2 = models.ImageField(blank=True,null=True , upload_to='Products/')
    img3 = models.ImageField(blank=True,null=True , upload_to='Products/')
    img4 = models.ImageField(blank=True,null=True , upload_to='Products/')
    
    quantity = models.IntegerField(blank=True , null=True )
    
    description = models.TextField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    material = models.CharField(blank=True, null=True,max_length=50)
    mass = models.FloatField(blank=True, null=True)
    condition = models.CharField(blank=True, null=True,max_length=50)
    SKU = models.IntegerField(blank=True , null=True , unique=True)
    warranty = models.IntegerField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now=True , blank=True , null=True)
    
    def __str__(self):
        return f"{self.name}"

    @property
    def cover_url(self):
        if self.cover:
            return self.cover.url
        else:
            return f"https://lallahoriye.com/wp-content/uploads/2019/04/Product_Lg_Type.jpg"

    @property
    def in_stock(self):
        return self.quantity > 0
    
