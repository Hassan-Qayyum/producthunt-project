from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.utils import timezone


def home(request):
    products = Product.objects.all()
    return render(request,'products/home.html',{'products':products})

@login_required
def create(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.user_id = request.user
            product.title = request.POST['title']
            product.body = request.POST['body']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            if request.POST['url'].startswith("http://") or request.POST['url'].startswith("https://"):
                product.url = request.POST['url']
            else:
                product.url = 'http://'+request.POST['url']
            product.save()
            return redirect('detail', str(product.id))
        else:
            return render(request,'products/create.html',{'error':'All Fields are required.'})
    else:
        return render(request,'products/create.html')

@login_required(login_url='/accounts/signup')
def detail(request,id):
    product=get_object_or_404(Product,pk=id)
    if request.method=='POST':
        product.votes_total +=1
        product.save()
        return redirect('detail',product.id)
    return render(request,'products/detail.html',{'product':product})
