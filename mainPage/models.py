from django.db import models
from datetime import datetime
from . import helperFunctions


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







class Kantar(models.Model):
    kantar1 = models.FloatField(verbose_name="Kantar 1")
    kantar2 = models.FloatField(verbose_name="Kantar 2")
    kantar3 = models.FloatField(verbose_name="Kantar 3", null=True, blank=True)
    kantar4 = models.FloatField(verbose_name="Kantar 4", null=True, blank=True)
    kantar5 = models.FloatField(verbose_name="Kantar 5", null=True, blank=True)
    kantar6 = models.FloatField(verbose_name="Kantar 6", null=True, blank=True)
    tarih = models.DateTimeField(verbose_name="Tarih", default=datetime.now, blank=True, null=True)
    tedarikci = models.ForeignKey(Tedarikci, on_delete=models.DO_NOTHING, verbose_name="Tedarikçi")
    note=models.TextField(verbose_name="Not",null=True,blank=True,max_length=180)
    odeme=models.CharField(max_length=100,verbose_name="Ödeme yapıldı mı?",choices=
                           [('EVET','EVET'),('HAYIR','HAYIR')])
    nakliyat=models.CharField(max_length=100,verbose_name="Taşıma",choices=
                           [('PP','PP'),('Ted','Ted')])
    def __str__(self):
        return f'Kantar {str(self.id)} : {str(self.tarih)[:16]} / {self.tedarikci}'


class MalzemeGiris(models.Model):
    kantarId = models.ForeignKey(Kantar, on_delete=models.DO_NOTHING, verbose_name="Kantar ID")
    malzemeTipi = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Tipi")
    brut = models.FloatField(verbose_name="Brüt Ağırlık")
    hurda = models.FloatField(verbose_name="Hurda Ağırlık")
    net = models.FloatField(verbose_name="Net Ağırlık")
    birimFiyat = models.FloatField(verbose_name="Birim Fiyat")

class MalAlim(models.Model):
    mal = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü")
    miktar = models.FloatField(verbose_name="Ağırlık")
    hurda = models.FloatField(verbose_name="Hurda")
    birimFiyat = models.FloatField(verbose_name="Birim Fiyat")
    kantar=models.ForeignKey(Kantar,on_delete=models.DO_NOTHING,verbose_name="Kantar tartım numarası")

    def __str__(self):
        return f'{str(self.id)} nolu alım : {str(self.miktar)}kg {str(self.mal)}'


class musteri(models.Model):
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