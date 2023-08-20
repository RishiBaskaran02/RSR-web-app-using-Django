"""RSRsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
from APP import views



urlpatterns = [
    path('admin/', admin.site.urls), 
    path('Homepage/', views.Homepage),
    path('Login/', views.Login),
    path('register/', views.register),
    path('Logout/',views.Logout),
    path('Products/', views.Products),
    path('About/', views.About),
    path('Contact/', views.Contact),
    path('Account/', views.Account),
    path('adminLogout/',views.adminLogout),
    # newly done
    path('Profileedit/', views.Profileedit, name='Profileedit'),
    path('PassCheck/',views.PassCheck),
    path('UpdateAccount/',views.UpdateAccount),

    path('Verification/', views.Verificationn),
    path('adminVerification/',views.adminVerification),
    path('openFile/',views.openFile),
    path('makeVerify/',views.makeVerify),
    # upto this
    
    
    path('Forgot/', views.Forgot),
    path('Adminhome/', views.Adminhome),
    path('OfficeLogin/', views.OfficeLogin),
 

    path('office/',views.office),
    path('padmin/',views.productsadmin),
    path('padmin2/',views.productsadmin2),


    path('Oficehome/',views.Officehome),
]
