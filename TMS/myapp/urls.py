from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginUser, name='login'),
    path('index', views.index, name='index'),
    path('logout', views.logoutUser, name='logout'),
    path('tenantregister', views.tenantregister, name='tenantregister'),
    path('tenantlist', views.tenantlist, name='tenantlist'),
    path('registerproperty', views.registerproperty, name='registerproperty'),
    path('propertylist', views.propertylist, name='propertylist'),
    path('registerlandlord', views.registerlandlord, name='registerlandlord'),
    path('landlordlist', views.landlordlist, name='landlordlist'),
    path('registerhouse', views.registerhouse, name='registerhouse'),
    path('houselist', views.houselist, name='houselist'),
    path('addhouse', views.addhouse, name='addhouse'),
    path('allocated', views.allocated, name='allocated'),
    path('payrent', views.payrent, name='payrent'),
    path('paymentstatus', views.paymentstatus, name='paymentstatus'),
    path('turnover', views.turnover, name='turnover'),
    path('duelist', views.duelist, name='duelist'),
    path('invoice', views.invoice, name='invoice'),
]
