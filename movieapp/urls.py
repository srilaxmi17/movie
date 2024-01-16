from movieapp import views
from django.urls import path

urlpatterns= [path('',views.register,name='register'),
             path('index',views.index,name='index'),
             path('login',views.login,name='login'),
             path('logout',views.logout,name='logout'),
             path('feedback',views.feedback,name='feedback'),
             path('select/<int:Category_id>',views.select,name='select'),
             path('watch/<int:id>',views.watch,name='watch'),
             path('reviews/<int:id>',views.reviews,name='reviews'),
             path('comments/<int:id>',views.comments,name='comments'),
             path('trailer',views.trailer,name='trailer'), 
             path('about',views.about,name='about'),
             path('pricing',views.pricing,name='pricing'),
            #  path('my_plan/<int:user_id>',views.my_plan,name='my_plan'),
             path('payment/<int:id>',views.payment,name='payment'),
             path('contact',views.contact,name='contact'),
             ]
