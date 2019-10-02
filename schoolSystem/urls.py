"""schoolSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.conf import settings

urlpatterns = [
    #path('',include('studentinfo.urls')),
    path('',admin.site.urls),
    #path('admin/', admin.site.urls),
    path('useraccounts/',include('user_accounts.urls')),
    path('payment/', include('payment.urls')),
    path('accounts/password_reset/',PasswordResetView.as_view(),name='password_reset'),
    path('accounts/password_reset/done/',PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('accounts/password_reset/confirm/',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path(r'^', include('django.contrib.auth.urls')),

]

admin.site.site_header = 'My Home Page'
admin.site.site_title = 'Main Title |'
admin.site.index_title = 'Index'
admin.site.index_title = 'Index'