# Create your views here.
from django.shortcuts import HttpResponse, render
from Model import models  # 导入models文件

# def index(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # 将数据保存到数据库
#         models.UserInfo.objects.create(user=username, pwd=password)
#
#         # 从数据库中读取所有数据，注意缩进
#     data_list = models.UserInfo.objects.all()
#
#     packageurl = request.POST.get("packageurl")
#     devicesnumber = request.POST.get("devicesnumber")
#     eamil = request.POST.get("eamil")
#
#
#
#
#
#
#
#
#
#
#
#     return render(request, 'index.html', {'run': data_list})











def platform(request):
    context = {}
    context['hello'] = 'Hello World!'

    return render(request, 'index1.html', context)
