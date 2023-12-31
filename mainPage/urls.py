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
    path('al/kayitlar', views.queryTable, name="buyQuery"),
    path('sat', views.sell, name="sat"),
    path('al/son/<int:kantarID>', views.finalizeBuy, name="finalizeBuy"),
    path('redirect/<int:kantarID>', views.redirectToKantarEdit, name="redirect"),
    path('redirectToAlim/<int:alimID>', views.redirectToAlimEdit, name="redirectAlim"),

]
