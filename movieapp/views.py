from django.shortcuts import render,redirect
from movieapp.models import *
from django.contrib.auth.models import User
from datetime import datetime,timedelta
# Create your views here.

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        contact=request.POST['contact']
        email=request.POST['email']
        password=request.POST['password']
        Register.objects.create(Name=name,Age=age,Contact=contact,E_Mail=email,Password=password)
    return render(request,'register.html')   

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if Register.objects.filter(E_Mail = email, Password = password).exists():
                data = Register.objects.filter(E_Mail = email, Password = password).values('Name', 'Age', 'Contact', 'id').first()
                request.session['u_name'] = data['Name']
                request.session['u_age'] = data['Age']
                request.session['u_contact'] = data['Contact']
                request.session['u_email'] = email
                request.session['user_id'] = data['id']
                current_date=datetime.now().date()
                print(current_date)
                user_id=request.session.get('user_id')
                user_status=Payment.objects.filter(user=user_id, plan_status='active')
                print('user_status= ',user_status)
                for i in user_status:
                    if current_date<=i.plan_expiry:
                        print('expiry= ',i.plan_expiry)   
                        return redirect('index')
                    else:
                        i.plan_status='inactive'
                        i.save()
                        return redirect('pricing')
                else:
                    return redirect('pricing')
        elif User.objects.filter(email=email).exists():
            admin_details=User.objects.get(email=email)
            check_pwd=admin_details.check_password(password)
            if check_pwd:
                return redirect('admindex')
            else:
                return redirect('login')       

        else:
            return redirect('login')    
    return render(request,'login.html')     

def index(request):
    user_id=request.session.get('user_id')
    username=request.session['u_name']
    category=Category.objects.all()
    movies=Movies.objects.all()
    notification=Notification.objects.all().order_by('-id')
    context={'category':category, 'movies':movies,'username':username,'notification':notification}
    return render(request,'index.html',context)                         

def select(request, Category_id):
    category=Category.objects.all()
    category_name=Category.objects.filter(id=Category_id)
    movies_category = Movies.objects.filter(Category=Category_id)
    context={'movies_category':movies_category,'category':category,'category_name':category_name}
    return render(request, 'select.html', context)

def about(request):
    category=Category.objects.all()
    context={'category':category}
    return render(request,'about.html',context)  

def contact(request):
    category=Category.objects.all()
    context={'category':category}
    return render(request,'contact.html',context)    

def trailer(request):
    category=Category.objects.all()
    movies=Movies.objects.all()
    context={'movies':movies,'category':category}
    return render(request,'trailer.html',context)   

def watch(request,id):
    movies_category=Movies.objects.filter(id=id)
    movies=Movies.objects.all()
    category=Category.objects.all()
    cast=Cast.objects.filter(movie_id=id)
    reviews=Reviews.objects.filter(movie_id=id)
    comments=Comments.objects.filter(movie_id=id)
    context={'movies_category':movies_category,'movies':movies,'reviews':reviews,'comments':comments,'category':category,'cast':cast}
    return render(request,'watch.html',context)

def reviews(request,id):
    user_id=request.session.get('user_id')
    if request.method=='POST':
        add_reviews=request.POST['add_reviews']
        rating=request.POST['rate']
        Reviews.objects.create(user_name=Register.objects.get(id=user_id),movie_id=Movies.objects.get(id=id),add_reviews=add_reviews,rating=rating)
        return redirect('index')
    return render(request,'watch.html')

def comments(request,id):
    user_id=request.session.get('user_id')
    if request.method=='POST':
        add_comments=request.POST['comments']
        Comments.objects.create(username=Register.objects.get(id=user_id),movie_id=Movies.objects.get(id=id),add_comments=add_comments)   
        return redirect('index')
    return render(request,'watch.html')
        
def feedback(request):
    user_id=request.session.get('user_id')
    if request.method=='POST':
        subject=request.POST['subject']
        message=request.POST['message']
        Feedback.objects.create(u_name=Register.objects.get(id=user_id),add_subject=subject,add_message=message)
        return redirect('index')
    return render(request,'index.html')    

def pricing(request):
    subscription=Subscription.objects.all()
    context={'subscription':subscription}
    return render(request,'pricing.html',context)

def payment(request,id):
    user_id=request.session.get('user_id')
    subscription=Subscription.objects.filter(id=id)
    sub=Subscription.objects.get(id=id)
    if sub.plan=='Basic':
        current_date=datetime.now()
        plan_expiry=current_date+timedelta(days=7)
    elif sub.plan=='Standard':
        current_date=datetime.now()
        plan_expiry=current_date+timedelta(days=30)
    elif sub.plan=='Premium':
        current_date=datetime.now()
        plan_expiry=current_date+timedelta(days=60)    
    else:
        pass  
    plan_status='inactive'
    if request.method=='POST':
        plan=request.POST['plan']
        card_number=request.POST['card_number']
        expiry_date=request.POST['expiry_date']
        cvv=request.POST['cvv']
        plan_status='active'
        Payment.objects.create(user=Register.objects.get(id=user_id),card_number=card_number,cvv=cvv,plan=Subscription.objects.get(plan=plan),expiry_date=expiry_date,plan_expiry=plan_expiry,plan_status=plan_status)
        return redirect('index')
    context={'subscription':subscription,'plan_expiry':plan_expiry,'id':id}
    return render(request,'payment.html',context)    


def logout(request):
    del request.session['u_name']
    del request.session['u_age']
    del request.session['u_contact']
    del request.session['u_email']
    del request.session['user_id']
    return redirect('login')

def my_plan(request,user_id):
    user_id=request.session.get('user_id')
    payment=Payment.objects.filter(id=user_id)
    return render(request,'my_plan.html')