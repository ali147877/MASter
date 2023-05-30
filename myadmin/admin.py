from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from web3 import Web3


# Register your models here.
class MyAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('add_certificate/', self.my_page_view),
        ]
        return my_urls + urls

    def my_page_view(self, request):
        return render(request, 'myadmin/add_certificate_page.html')


my_admin_site = MyAdminSite()
