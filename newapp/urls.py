from . import views
from django.urls import path

urlpatterns = [
    path('',views.new,name='new'),
   # path('about/',views.about,name='about'),
    #path('contact/',views.contact,name='contact'),
    #path('detail/',views.detail,name='detail')
]
