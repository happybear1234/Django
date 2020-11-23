"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.shortcuts import HttpResponse, render, redirect


def longin(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        if u == 'root' and p == '123':
            return redirect('/index')
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})


def index(request):
    # return HttpResponse('index')
    return render(
        request,
        'index.html',
      {
          'name': 'alex',
          'users': ['李志', '李杰'],
          'user_dict': {'k1': 'v1', 'k2': 'v2'},
          'user_list_dict': [
              {'id': '1', 'name': 'alex1', 'email': '0001'},
              {'id': '2', 'name': 'alex2', 'email': '0002'},
              {'id': '3', 'name': 'alex3', 'email': '0003'}

          ]
      })


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', longin),
    path('index/', index)
]
