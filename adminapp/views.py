from django.shortcuts import render,redirect
from adminapp.models import *
from movieapp.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def admindex(request):
    return render(request,'admindex.html') 

def message(request):
    feedback=Feedback.objects.all()
    context={'feedback':feedback}
    return render(request,'message.html',context)

def user(request):
    userinfo=Register.objects.all()
    context={'userinfo':userinfo}
    return render(request,'user.html',context) 

def display(request):
    movies=Movies.objects.all()
    cast=Cast.objects.all()
    context={'movies':movies,'cast':cast}
    return render(request,'display.html',context)  

def edit(request,edit_id):
    edit=Movies.objects.filter(id=edit_id)
    category=Category.objects.all()
    context={'edit':edit,'category':category}
    return render(request,'edit.html',context)         

def update(request,edit_id):
        if request.method=='POST':
            category=request.POST['category']
            c_id=Category.objects.get(Category=category)
            movie_name=request.POST['movie_name']
            movie_year=request.POST['movie_year']
            # movie_cast=request.POST['movie_cast']
            movie_director=request.POST['movie_director']
            movie_trailer=request.POST['movie_trailer']
            try:
                img=request.FILES['movie_image']
                mov_fil=request.FILES['movie_file']
                fs1=FileSystemStorage()
                file1=fs1.save(img.name,img)
                fs2=FileSystemStorage()
                file2=fs2.save(mov_fil.name,mov_fil)
            except MultiValueDictKeyError:
                file1=edit.objects.get(id=edit_id).Movie_image 
                file2=edit.objects.get(id=edit_id).Movie_file 
            Movies.objects.filter(id=edit_id).update(Category=c_id,Movie_name=movie_name,Movie_year=movie_year,Movie_image=file1,Movie_director=movie_director,Movie_trailer=movie_trailer,Movie_file=file2)
            return redirect('display')  
        return render(request,'edit.html')   

def delete(request,edit_id):
    Movies.objects.filter(id=edit_id).delete()
    return redirect('display')               

def category_form(request):
    if request.method=='POST':
        category=request.POST['category']
        Category.objects.create(Category=category)
    return render(request,'category_form.html')

def cast(request):
    movies=Movies.objects.all()
    context={'movies':movies}
    if request.method=='POST':
        cast_name=request.POST['cast_name']        
        cast_img=request.FILES['cast_img'] 
        cast_movie=request.POST['cast_movie']
        cast_mov=Movies.objects.get(Movie_name=cast_movie)
        Cast.objects.create(movie_id=cast_mov,cast_name=cast_name,cast_img=cast_img)
    return render(request,'cast.html',context)    

def movies_form(request):
    category=Category.objects.all()
    context={'category':category}    
    if request.method=='POST':
        category=request.POST['category']
        c_id=Category.objects.get(Category=category)
        movie_name=request.POST['movie_name']
        movie_year=request.POST['movie_year']
        movie_image=request.FILES['movie_image']
        movie_file=request.FILES['movie_file']
        movie_director=request.POST['movie_director']
        movie_trailer=request.POST['movie_trailer']
        Movies.objects.create(Category=c_id,Movie_name=movie_name,Movie_image=movie_image,Movie_year=movie_year,Movie_director=movie_director,Movie_trailer=movie_trailer,Movie_file=movie_file)
    return render(request,'movies_form.html',context)

def sample_form(request):
    return render(request,'sample_form.html') 

def notification(request):
    if request.method=='POST':
        update=request.POST['update']
        Notification.objects.create(updates=update)
    return render(request,'notification.html') 

def plan(request):
    if request.method=='POST':
        p_name=request.POST['p_name']
        amount=request.POST['amount']
        validity=request.POST['validity']
        availability=request.POST['availability']
        resolution=request.POST['resolution']
        Subscription.objects.create(plan=p_name,amount=amount,validity=validity,resolution=resolution,availabilty=availability) 
    return render(request,'plan.html')              

def admindex(request):
    return render(request,'admindex.html')

def u_payment(request):
    payment=Payment.objects.all()
    context={'payment':payment}
    return render(request,'u_payment.html',context)

def ad_logout(request):
    return redirect('login')    