from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Images
# Create your views here.


def add_image(request):
    
    return render (request,'feedpage.html')

def create_entry(request):
    c = request.POST['caption']
    i = request.FILES['image_data']
    cu = request.session["current_user"]
    image_details = Images(caption=c,image_data=i,user=cu)
    image_details.save()
    return redirect ('/feedpage/show_images')

def show_images(request):
    all_images = Images.objects.raw("SELECT *FROM feedpage_images")
    context ={
        "images":all_images
    }
    return render (request,'display.html',context)
    '''
    for i in all_images:
        print(i.caption,i.image_data)
    '''
    