# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.transaction import commit
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import DepartmentInfo, UserInfo, UserRole


def emp_add(request):
    if request.method == 'GET':
        return render(request, 'emp_add.html')
    else:
        user_name = request.POST.get('userName', None)
        user_sex = request.POST.get('userSex', None)
        user_num = request.POST.get('userNum', None)
        user_age = request.POST.get('userAge', None)
        user_pw = request.POST.get('userPw', None)
        user_nation = request.POST.get('userNation', None)
        user_diploma = request.POST.get('userDiploma', None)
        is_married = request.POST.get('isMarried', None)
        # department = request.POST.get('departmentId', None)
        # role = request.POST.get('roleId', None)
        user_tel = request.POST.get('userTel', None)
        user_intest = request.POST.get('userIntest', None)
        user_bankcard = request.POST.get('userBankcard', None)
        user_mobile = request.POST.get('userMobile', None)
        user_idnum = request.POST.get('userIdnum', None)
        user_addtime = request.POST.get('userAddtime', None)
        user_address = request.POST.get('userAddress', None)
        user_addman = request.POST.get('userAddman', None)
        user_email = request.POST.get('userEmail', None)
        empadd1 = 'NOT'
        try:
            empadd1 = UserInfo.objects.get(user_name=user_name,user_num=user_num,user_sex=user_sex,user_age=user_age,
                                           user_pw=user_pw,user_nation=user_nation,user_diploma=user_diploma,is_married=is_married,
                                           user_tel=user_tel,user_intest=user_intest,
                                           user_bankcard=user_bankcard,user_mobile=user_mobile,user_idnum=user_idnum,
                                           user_addtime=user_addtime,user_address=user_address,user_addman=user_addman,
                                           user_email=user_email)
        except UserInfo.DoesNotExist:
            empadd2 = UserInfo.objects.create(user_name=user_name,user_num=user_num,user_sex=user_sex,user_age=user_age,
                                           user_pw=user_pw,user_nation=user_nation,user_diploma=user_diploma,is_married=is_married,
                                           user_tel=user_tel,user_intest=user_intest,
                                           user_bankcard=user_bankcard,user_mobile=user_mobile,user_idnum=user_idnum,
                                           user_addtime=user_addtime,user_address=user_address,user_addman=user_addman,
                                           user_email=user_email)
        if empadd1 != 'NOT':
            return HttpResponse('记录已存在')
        elif empadd2:
            return HttpResponse('添加成功')
        else:
            return HttpResponse('添加失败')






def dept_add(request):
    if request.method == 'GET':
        return render(request, 'dept_add.html')
    else:
        dep_name = request.POST.get('departmentName', None)
        dep_desc = request.POST.get('departmentDesc', None)
        depart1 = 'NOT'
        try:
            depart1 = DepartmentInfo.objects.get(department_name=dep_name, department_desc=dep_desc)
        except DepartmentInfo.DoesNotExist:
            depart2 = DepartmentInfo.objects.create(department_name=dep_name, department_desc=dep_desc)
        if depart1 != 'NOT':
            return HttpResponse('记录已存在')
        elif depart2:
            return HttpResponse('添加成功')
        else:
            return HttpResponse('添加失败')

#
def role_add(request):
    if request.method == 'GET':

        return render(request,'role_add.html')
    else:
        role = request.POST.get('roleName',None)
        role_pow = request.POST.get('rolePower',None)
        try:
            role_name = UserRole.objects.get(role_name=role)
            role_power = UserRole.objects.get(role_power=role_pow)
        except UserRole.DoesNotExist:
            role_name = UserRole.objects.create(role_name=role)
            role_power = UserRole.objects.create(role_power=role_pow)
        return HttpResponseRedirect('/adminlist/role_add.html')