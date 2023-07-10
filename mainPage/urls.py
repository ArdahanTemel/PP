
from django.contrib import admin
from django.urls import path
from . import views
from . import models

# def getLatestentryNumber():
#     latestRecordId = models.Alimlar.objects.all().latest("alimKodu").alimKodu
#     # print(latestRecordId)
#     latestPlusOne = latestRecordId + 1
#     return latestPlusOne

urlpatterns = [
    path("", views.mainPageView, name="mainPage"),
    path("login", views.loginView, name="login"),
    path("logout", views.logoutView, name="logout"),
    path("al/<int:id>", views.buy1, name="buy"),

]
