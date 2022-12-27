from django.contrib import admin
from login_test.models import MyUser


# Register your models here.

class MyAdmin(admin.ModelAdmin):
    list_display = ["User", "status"]  # 展示的内容,名称必须为 list_display
    search_fields = ["User__username", "status"]  # 配置检索字段。配置了的字段才能被检索。
                                                  # "User__username" : User 是 Myuser 表里的外键，username 这是这个外键中的字段

admin.site.register(MyUser, MyAdmin)
