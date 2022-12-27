"""untitled6 URL Configuration

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
from django.urls import path
from login_test.views import login_success, jq, register_user, user_status, status_all, update_user
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='login.html')),
    path('login_success', login_success),
    path('exit', LogoutView.as_view(next_page='/')),  # 配置登出后，跳转到根页面
    path('JQuery.js', jq),
    path('register_user', register_user),

    path('status',user_status),
    path("status_all",status_all),
    path("update_user",update_user)

]
