from django.shortcuts import render
from .models.product import Product
from .models.catagory import Catagory
# Create your views here.
def index(request):
    task=None
    catagory=Catagory.objects.all()
    customer_ID=request.GET.get('catagory')
    print(customer_ID)
    if customer_ID:
        task=Product.objects.filter(catagory=customer_ID)
    else:
        task=Product.objects.all()
    data={}   
    data["task"]=task
    data["catagory"]=catagory
    return render(request,"index.html",data)



def gallery(request):
    task=Product.objects.all()
    return render(request,"gallery.html",{"task":task})
    