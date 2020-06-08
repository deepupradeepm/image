from django.shortcuts import render,redirect
from PIL import Image
from .models import Emp
from django.contrib import messages
# Create your views here.
def save_detail(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        ph=request.POST['ph']
        p=request.FILES['p']
        img1=Image.open(p)
        print(img1.size)
        h,w=img1.size
        # if h>300 and w>300:
        #     img1.resize(200,200)
        #     img1.save()
        #     messages.error(request,'image not valid')
        #     return redirect('home')
        Emp(name=name,email=email,ph=ph,image=p).save()
        messages.success(request, 'data is saved')
        return redirect('home')
    return render(request,'home.html')