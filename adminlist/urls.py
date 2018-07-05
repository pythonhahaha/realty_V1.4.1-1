#coding=utf-8


from django.conf.urls import url

from adminlist import views

urlpatterns = [
    # 添加员工
    url(r'emp_add.html/', views.emp_add),
    # 添加部门
    url(r'dept_add.html/', views.dept_add),
    # 添加角色
    url(r'^role_add.html', views.role_add),


]