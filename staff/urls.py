
from django.conf.urls import url

from staff import views

urlpatterns = [

    url(r'emp_list.html', views.emp_list),
    url(r'emp_edit.html',views.emp_edit),

    url(r'del_emp_list',views.del_emp_list),

    url(r'house_list.html', views.house_list),

    url(r'house_type_list.html', views.house_type_list),

    url(r'dept_list.html', views.dept_list),

    url(r'notice_list.html', views.notice_list),
]