from django.shortcuts import render , redirect
from .models import *
from users.models import *
from django.contrib.auth.models import User
from django.db.models import Q
from .utils import *
# Create your views here.

def testBuyer(request):
    user = User.objects.get(username = request.user.username)
    profile = Profile.objects.get( user = user)
    return profile.is_buyer


def home(request):
    if request.user.is_authenticated :
        username = request.user.username
        user = User.objects.get(username=username)
        try:
            profile = Profile.objects.get(user = user)
            categories = Category.objects.all()
            context = {
                "categories" : categories,
            }
            return render(request , "products/index.html" , context)
        except :
            return redirect("make-profile")
    else:
        categories = Category.objects.all()
        context = {
                "categories" : categories,
            }
        return render(request , "products/index.html" , context)


def category(request , title):
    search = ''
    category = Category.objects.get(title = title)
    
    categories = Category.objects.all()
    
    if request.GET.get('search') : 
        search = request.GET.get('search')
        
    mark = Mark.objects.all().filter(name__icontains = search)
    products = Product.objects.all().filter(category = category).distinct().filter( 
                                                Q(name__icontains = search) |
                                                Q(mark__in = mark) |
                                                Q())

    is_buyer = False
    if request.user.is_authenticated:
        is_buyer = testBuyer(request)
    
    costum_range , products = productPaginator(request , products , 9)
    
    context = {
        "costum_range" : costum_range ,
        "search":search,
        "category" : category,
        "categories":categories,
        "products" : products ,
        "is_buyer" : is_buyer,
    }
    return render(request , "products/category.html" , context)


def view_product(request , pk):
    product = Product.objects.get(pk = pk)
    category = Category.objects.get(title = product.category.title)
    products = Product.objects.all().filter(category = category).exclude(id__in= pk)[:4]
    
    
    is_buyer = False
    if request.user.is_authenticated:
        is_buyer = testBuyer(request)

    context = {
        "is_buyer" : is_buyer,
        "products" : products,
        "product" : product ,
    }
    return render(request , "products/product-page.html" , context)