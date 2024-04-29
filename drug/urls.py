from django.contrib import admin
from django.urls import path,include
from drug.views import log,reg,inindex,outindex,payment,inorder,outpayment,outorder

app_name='drug1'
urlpatterns = [
    
    path('', log, name='log'),
    path("reg/",reg,name='reg'),
    path("inindex/",inindex,name='inindex'),
    path("outindex/",outindex,name='outindex'),
    path("payment/",payment,name='payment'),
    path("inorder/",inorder,name='inorder'),
    path("outpayment/",outpayment,name='outpayment'),
    path("outorder/",outorder,name='outorder'),

    
]