"""config URL Configuration

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
from django.urls import path, include
from django.views.generic import TemplateView

from hos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='loginpage.html'), name='loginpage'),
    path('logout', views.logout, name='logout'),
    path('loginimpl', views.loginimpl, name='loginimpl'),
    path('base', TemplateView.as_view(template_name='base.html'), name='base'),

    path('index', views.index, name='index'),
    path('graph', views.graph, name='graph'),
    path('graph1', views.graph1, name='graph1'),

    path('doctors', views.doctors, name='doctors'),
    path('add-doctor', views.add_doctor, name='add-doctor'),
    path('docaddimpl', views.docaddimpl, name='docaddimpl'),
    path('doc_patientlist', views.doc_patientlist, name='doc_patientlist'),
    path('docdelete', views.docdelete, name='docdelete'),
    path('doc_delete_error', TemplateView.as_view(template_name='doc_delete_error.html'), name='doc_delete_error'),

    path('add_treatment', views.add_treatment, name='add_treatment'),
    path('treataddimpl', views.treataddimpl, name='treataddimpl'),

    path('add_chart', views.add_chart, name='add_chart'),
    path('chartaddimpl', views.chartaddimpl, name='chartaddimpl'),

    path('patients', views.patients, name='patients'),
    path('patientlist', TemplateView.as_view(template_name='patientlist.html'), name='patientlist'),
    path('add-patient', views.add_patient, name='add-patient'),
    path('patientaddimpl', views.patientaddimpl, name='patientaddimpl'),

    path('getchart', views.getchart, name='getchart'),
    path('chart', views.chart,name='chart'),

    path('hospitalstructure', views.hospitalstructure, name='hospitalstructure'),


    path('firstfloor', views.firstfloor, name='firstfloor'),
    path('secondfloor', views.secondfloor, name='secondfloor'),
    path('thirdfloor', views.thirdfloor, name='thirdfloor'),


    path('popup101.html', views.popup101, name='popup101.html'),
    path('popup102.html', views.popup102, name='popup102.html'),
    path('popup103.html', views.popup103, name='popup103.html'),
    path('popup201.html', views.popup201, name='popup201.html'),
    path('popup202.html', views.popup202, name='popup202.html'),
    path('popup203.html', views.popup203, name='popup203.html'),
    path('popup301.html', views.popup301, name='popup301.html'),
    path('popup302.html', views.popup302, name='popup302.html'),

    path('guest_popup101.html', views.guest_popup101, name='popup101.html'),
    path('guest_popup102.html', views.guest_popup102, name='popup102.html'),
    path('guest_popup103.html', views.guest_popup103, name='popup103.html'),
    path('guest_popup201.html', views.guest_popup201, name='popup201.html'),
    path('guest_popup202.html', views.guest_popup202, name='popup202.html'),
    path('guest_popup203.html', views.guest_popup203, name='popup203.html'),
    path('guest_popup301.html', views.guest_popup301, name='popup301.html'),
    path('guest_popup302.html', views.guest_popup302, name='popup302.html'),


# guest
    path('guest_index', views.guest_index, name='guest_index'),
    path('guest_doctors', views.guest_doctors, name='guest_doctors'),
    path('guest_hospitalstructure', views.guest_hospitalstructure, name='guest_hospitalstructure'),
    path('guest_firstfloor', views.guest_firstfloor, name='guest_firstfloor'),
    path('guest_secondfloor', views.guest_secondfloor, name='guest_secondfloor'),
    path('guest_thirdfloor', views.guest_thirdfloor, name='guest_thirdfloor'),

]
