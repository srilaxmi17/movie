from django.db import models

# Create your models here.

class Register(models.Model):
    Name=models.CharField(max_length=30)
    Age=models.IntegerField()
    Contact=models.IntegerField()
    E_Mail=models.EmailField()
    Password=models.CharField(max_length=10)

    def __str__(self):
        return f'{self.Name}'
    
class Category(models.Model):
    Category=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.Category}'
 

class Movies(models.Model):
    Category=models.ForeignKey(Category,on_delete=models.DO_NOTHING,null=True,blank=True)
    Movie_name=models.CharField(max_length=50)
    Movie_image=models.ImageField(upload_to='movies',default='null.jpg')
    Movie_year=models.IntegerField(null=True,blank=True)
    Movie_director=models.CharField(max_length=50)
    Movie_trailer=models.URLField(max_length=200)
    Movie_file=models.FileField(upload_to='movies',default='null.mp4')

    def __str__(self):
        return f'{self.id} : {self.Movie_name}'

class Cast(models.Model):
    movie_id=models.ForeignKey(Movies,on_delete=models.DO_NOTHING,null=True,blank=True)
    cast_name=models.CharField(max_length=50) 
    cast_img=models.ImageField(upload_to='cast',default='null.jpg')    

    def __str__(self):
        return f'{self.movie_id}'          

class Comments(models.Model):
    username=models.ForeignKey(Register,on_delete=models.DO_NOTHING,null=True,blank=True)
    movie_id=models.ForeignKey(Movies,on_delete=models.DO_NOTHING,null=True,blank=True)
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
    add_comments=models.CharField(max_length=500)

    def __str__(self):
        return f'{self.username}'
    
class Reviews(models.Model):
    user_name=models.ForeignKey(Register,on_delete=models.DO_NOTHING,null=True,blank=True)
    movie_id=models.ForeignKey(Movies,on_delete=models.DO_NOTHING,null=True,blank=True)
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
    add_reviews=models.CharField(max_length=500)
    rating=models.FloatField()   

    def __str__(self):
        return f'{self.user_name}' 

class Feedback(models.Model):
    u_name=models.ForeignKey(Register,on_delete=models.DO_NOTHING,null=True,blank=True)
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
    add_subject=models.CharField(max_length=200)
    add_message=models.CharField(max_length=500)

    def __str__(self):
        return f'{self.u_name}'

class Notification(models.Model):
    updates=models.TextField(max_length=100)    
    date=models.DateField(auto_now_add=True,null=True,blank=True)  

class Subscription(models.Model):
    plan=models.CharField(max_length=50)
    amount=models.FloatField()
    validity=models.CharField(max_length=50)
    resolution=models.CharField(max_length=100)
    availabilty=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.plan}'

class Payment(models.Model):
    user=models.ForeignKey(Register,on_delete=models.DO_NOTHING,null=True,blank=True)
    card_number=models.CharField(max_length=16)
    expiry_date=models.CharField(max_length=5)
    cvv=models.CharField(max_length=4)
    plan=models.ForeignKey(Subscription,on_delete=models.DO_NOTHING,null=True,blank=True)
    plan_expiry=models.DateField(null=True,blank=True)
    plan_status=models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.user}'