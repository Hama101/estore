from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage

def productPaginator(request , products , result):
    page = request.GET.get('page')
    paginator = Paginator(products , result)
    
    try :
        products = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        products = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        products = paginator.page(page)
    
    leftIndex , rightIndex = int (page) - 4 , int (page) + 4
    if leftIndex < 1 :
        leftIndex = 1
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages
    
    costum_range = range(leftIndex , rightIndex + 1)

    return costum_range , products