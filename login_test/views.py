from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from login_test.models import MyUser


@login_required
def login_success(request):
    print(request.user)
    return render(request, "login_success.html")


def jq(request):
    return render(request, "JQuery.js")


# 注册用户
def register_user(request):
    # 先创建外键的 Django 的 User
    try:
        d_user = User.objects.create(
            password=request.POST.get('password'),
            username=request.POST.get('username')
        )

        MyUser.objects.create(
            User=d_user,
            status="nothing"
        )

    # 用 json response 来返回 response 信息
    except  Exception as err_msg:  # 保存返回信息
        return JsonResponse({
            "result": False,
            "message": str(err_msg)
        })

    else:
        return JsonResponse({
            "result": True,
            "message": "成功注册"
        })


# 用户状态
def user_status(request):
    my_user = MyUser.objects.get(User=request.user)

    return render(request, "status.html", {
        "username": my_user.User.username,
        "status": my_user.status
    })


def status_all(request):
    if request.GET.get("keyword"):
        my_user = MyUser.objects.filter(User__username__contains=request.GET.get("keyword"))

    else:
        my_user = MyUser.objects.all()
    return render(request, "status_all.html",
                  {"myuser": my_user, })


def update_user(request):
    try:
        my_user = MyUser.objects.filter(User=request.user)
        my_user.update(status=request.POST.get("status"))

    # 用 json response 来返回 response 信息
    except  Exception as err_msg:  # 保存返回信息
        return JsonResponse({
            "result": False,
            "message": str(err_msg)
        })

    else:
        return JsonResponse({
            "result": True,
            "message": "成功修改"
        })
