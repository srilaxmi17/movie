from adminapp import views
from django.urls import path

urlpatterns= [path('admindex',views.admindex,name='admindex'),
            path('plan',views.plan,name='plan'),
            path('u_payment',views.u_payment,name='u_payment'),
            path('movies_form',views.movies_form,name='movies_form'),
            path('category_form',views.category_form,name='category_form'),
            path('cast',views.cast,name='cast'),
            path('display',views.display,name='display'),
            path('edit/<int:edit_id>',views.edit,name='edit'),
            path('update/<int:edit_id>',views.update,name='update'),
            path('delete/<int:edit_id>',views.delete,name='delete'),
            path('message',views.message,name='message'),
            path('user',views.user,name='user'),
            path('sample_form',views.sample_form,name='sample_form'),
            path('ad_logout',views.ad_logout,name='ad_logout'),
            path('notification',views.notification,name='notification'),
            ]
