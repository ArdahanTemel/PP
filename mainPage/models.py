from django.db import models
from datetime import datetime


# Create your models here.

class Tedarikci(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ad")
    surname = models.CharField(max_length=50, verbose_name="Soyad")
    idNumber = models.CharField(max_length=25, verbose_name="TC Kimlik No")
    adress = models.CharField(max_length=200, verbose_name="Adres")
    tax = models.CharField(max_length=100, verbose_name="Vergi Dairesi")
    mail1 = models.EmailField(max_length=100, verbose_name="E-mail 1")
    mail2 = models.EmailField(max_length=100, verbose_name="E-mail 2")
    phoneNumber1 = models.CharField(max_length=20, verbose_name="Telefon 1")
    phoneNumber2 = models.CharField(max_length=20, verbose_name="Telefon 2")
    IBAN = models.CharField(max_length=100, verbose_name="IBAN")
    bankNumber = models.CharField(max_length=100, verbose_name="Banka Hesap Numarası")
    bank = models.CharField(max_length=100, verbose_name="Banka")
    companyName = models.CharField(max_length=100, verbose_name="Şirket")

    def __str__(self):
        return self.name + " " + self.surname + " / " + self.companyName


class Hammadde(models.Model):
    rawMaterialName = models.CharField(max_length=200, verbose_name="Hammadde Tipi")
    isScrap = models.BooleanField(verbose_name="Değersiz / Hurda mı?", choices=[(1, 'EVET'), (0, 'HAYIR')])

    def __str__(self):
        return self.rawMaterialName


class Alimlar(models.Model):
    alimKodu = models.IntegerField(primary_key=True, verbose_name="ID")
    tedarikEden = models.ForeignKey(Tedarikci, on_delete=models.DO_NOTHING, verbose_name="Tedarikçi")
    mal = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü")
    miktar = models.FloatField(verbose_name="Ağırlık (kg)")
    tarih = models.DateTimeField(verbose_name="Tarih", default=datetime.now)
    birimFiyat = models.FloatField(verbose_name="Birim Fiyat")
    alimKoduGenel = models.IntegerField(verbose_name="Alım Kodu")

    def __str__(self):
        return str(self.tarih) + "-" + str(self.miktar) + "-" + str(self.tedarikEden)+"-"+str(self.alimKodu)+"-"+str(self.alimKoduGenel)


class Alimlar_Kirilim(models.Model):
    alimKodu = models.CharField(primary_key=True, verbose_name="ID", max_length=100)
    tedarikEden = models.ForeignKey(Tedarikci, on_delete=models.DO_NOTHING, verbose_name="Tedarikçi")
    mal = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü")
    miktar = models.FloatField(verbose_name="Ağırlık (kg)")
    tarih = models.DateTimeField(verbose_name="Tarih",default=datetime.now)
    birimFiyat = models.FloatField(verbose_name="Birim Fiyat")
    alimKoduGenel = models.IntegerField(verbose_name="Alım Kodu")

    def __str__(self):
        return str(self.tarih) + "-" + str(self.miktar) + "-" + str(self.tedarikEden)
