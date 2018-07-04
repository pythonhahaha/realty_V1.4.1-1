# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from home.models import UserInfo
from django.shortcuts import render

# Create your views here.
# 员工信息
def emp_list(request):
    staff_list = UserInfo.objects.all()
    return render(request, 'emp_list.html', {'staff_list': staff_list})
# 修改员工信息
def emp_edit(request):
    return render(request,'emp_edit.html')
# 删除员工信息
def del_emp_list(request):
    eid = request.GET.get('staff_id')
    UserInfo.objects.get(user_id=eid).delete()
    return HttpResponseRedirect('/staff/emp_list.html')


def house_list(request):
    return render(request, 'house_list.html')


def house_type_list(request):
    return render(request, 'house_type_list.html')


def dept_list(request):
    return render(request, 'dept_list.html')


def notice_list(request):
    return render(request, 'notice_list.html')