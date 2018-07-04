# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from re import match

from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *

# Create your views here.
# 客户信息
def customer_list1(request):

    cust_list = CustomerInfo.objects.all()

    return render(request, 'customer_list1.html', {'cust_list': cust_list})


 # 客户信息编辑
def customer_edit(request):
    cust_list_bj = CustomerInfo.objects.create()
    return render(request, 'customer_edit.html', {'cust_list_bj': cust_list_bj})

# 客户详情
def customer_detail(request):
    return render(request, 'customer_detail.html')

# 添加客户信息
def customer_add(request):

    return render(request,'customer_add.html')


# 客户分配信息目录
def customer_distribute_list(request):
    cust_dist_list = CustomerLinkreord.objects.all()
    return render(request, 'customer_distribute_list.html',{'cust_dist_list':cust_dist_list})

# 分配所选客户信息
def customer_distribute(request):
    return render(request, 'customer_distribute.html')


# 客户关怀信息目录
def customer_care_list(request):
        cust_care_list = CustomerCare.objects.all()
        return render(request, 'customer_care_list.html', {'cust_care_list': cust_care_list})
# 客户关怀搜索
def customercare_search(request):
    queryType = request.POST.get('queryType')
    queryType = int(queryType)
    customerInput = request.POST.get('customerInput')
    if queryType == 1:
        cname = customerInput
        if cname:
            ca = CustomerInfo.objects.filter(cname=cname)
            if ca:
                care=CustomerCare.objects.filter(car_tomen=ca[0])
                if care:
                    return render(request,'customer_care_list.html',{'care_list':care})

            else:
                return  HttpResponse('<script>alert("不存在，请输入正确的名字!");location.href="/client/customer_care_list.html";</script>')
        else:
            return HttpResponse('<script>alert("不能为空");location.href="/client/customer_care_list.html";</script>')

    elif queryType == 2:
        car_theme = customerInput
        if car_theme:
            ct = CustomerCare.objects.filter(car_theme=car_theme)
            if ct:
                return render(request,'customer_care_list.html',{'care1':ct})
            else:
                return HttpResponse(
                    '<script>alert("不存在，请输入正确的主题!");location.href="/client/customer_care_list.html";</script>')

        else:
            return HttpResponse('<script>alert("不能为空");location.href="/client/customer_care_list.html";</script>')

    elif queryType == 3:
        car_way = customerInput
        if car_way:
            cw = CustomerCare.objects.filter(car_way=car_way)
            if cw:
                return render(request,'customer_care_list.html',{'care1':cw})
            else:
                return HttpResponse(
                    '<script>alert("不存在，请输入正确的方式!");location.href="/client/customer_care_list.html";</script>')
        else:
            return HttpResponse('<script>alert("不能为空");location.href="/client/customer_care_list.html";</script>')


# 客户关怀修改
def customer_care_edit(request):
    if request.method == 'GET':
        return render(request, 'customer_edit.html')
    else:
        care_edit = request.GET.get('care_edit')
        customerForUser



    # nid = request.GET.get('care_edit')
    # CustomerCare.objects.get(care_id=nid).update()

    # return HttpResponseRedirect('/client/customer_care_list.html')
            # 想修改删了重新添加

# 删除客户关怀
def del_customer_care(request):
    nid = request.GET.get('care_id')
    CustomerCare.objects.get(care_id=nid).delete()
    return HttpResponseRedirect('/client/customer_care_list.html')
# 添加客户关怀
def customer_care_add(request):
    if request.method == 'GET':
        return render(request, 'customer_care_add.html')
    else :
        if request.method=='POST':
            # care_nexttime = request.POST.get('careNexttime','')
            care_people = request.POST.get('carePeople','')
            care_theme = request.POST.get('careTheme','')
            care_way = request.POST.get('careWay','')
            care_remark = request.POST.get('careRemark','')
            depart1 = 'NOT'
            try:
                depart1 = CustomerCare.objects.get(care_people=care_people,care_theme=care_theme,care_way=care_way,care_remark=care_remark)
            except CustomerCare.DoesNotExist:
                depart2 = CustomerCare.objects.create(care_people=care_people,care_theme=care_theme, care_way=care_way, care_remark=care_remark)
            if depart1 != 'NOT':
                return HttpResponse('记录已存在')
            elif depart2 :
                return HttpResponseRedirect('/client/customer_care_list.html')
            else:
                return HttpResponse('添加失败')

# 客户类型信息目录
def customer_type_list(request):
    cust_type_list = CustomerType.objects.all()
    return render(request, 'customer_type_list.html',{'cust_type_list':cust_type_list})

# 客户状态信息目录
def customer_state_list(request):
    cust_stat_list = CustomerStatus.objects.all()
    return render(request, 'customer_state_list.html',{'cust_stat_list': cust_stat_list})

# 客户来源信息目录
def customer_source_list(request):
    cust_source_list = CustomerSource.objects.all()
    cust_source_list_del = CustomerSource .objects.filter()
    return render(request, 'customer_source_list.html', {'cust_source_list':cust_source_list},{'cust_source_list_del':cust_source_list_del})

    print(cust_source_list)

# 客户来源信息添加
def customer_source_add(request):
    if request.method == 'GET':
        return render(request, "customer_source_add.html")
    else:
        source_name = request.POST.get('sourceName', None)

        try:
            source1 = CustomerSource.objects.get(source_name=source_name)
        except CustomerSource.DoesNotExist:
            source2 = CustomerSource.objects.create(source_name=source_name)

    return HttpResponseRedirect('/client/customer_source_list')

# 客户来源信息删除
def customer_source_list_dele(request):
    sourc_id = request.GET.get('sourceId', None)
    sourc_id = int(sourc_id)
    CustomerSource.objects.filter(source_id=sourc_id).delete()
    return HttpResponseRedirect('/client/customer_source_list.html')

# 客户查询
def customer_source_list_find(request):
    if request.method == 'GET':
        cust_source_list = CustomerSource.objects.all()
        return render(request, 'customer_source_list.html', {'cust_source_list': cust_source_list})
    else:
        source_name = request.POST.get('SourceName', None)
        source_name = CustomerSource.objects.filter(source_name=source_name)
        if source_name:
            return render(request, "customer_source_list.html", {'cust_source_list': source_name})
        else:
            return HttpResponseRedirect('/client/customer_source_list')

# 分页展示
def customer_source_list_tab(request, num=1):
    # 获取当前页吗
    num = int(num)
    # 查询所有帖子
    cust_posts = CustomerSource.objects.order_by('-created')
    # 创建分页器对象
    cust_sourc_tab = Paginator(cust_posts, per_page=1)
    # 获取当前页的数据
    cust_list_post = cust_sourc_tab.page(num)
    # 每页显示的页码范围
    cust_tab_begin = (num-int(match.ceil(10.0/2)))
    if cust_tab_begin < 1:
        cust_tab_begin = 1
    # 每页结束码
    cust__tab_end = cust_tab_begin + 9
    if cust__tab_end > cust_sourc_tab.num_pages:
        cust__tab_end = cust_sourc_tab.num_pages
    if cust__tab_end <= 10:
        cust_tab_begin = 1
    else: cust_tab_begin = cust__tab_end - 9

    cust_paglist = range(cust_tab_begin,cust__tab_end+1)

    return render(request,'customer_source_list.html',{'cust_list_post':cust_list_post,'cust_paglist':cust_paglist,'num':num,'cust_posts':cust_posts})