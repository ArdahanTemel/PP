from django.db import models
from datetime import datetime
from . import helperFunctions


# Create your models here.

class Tedarikci(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ad Soyad / Şirket")
    idNumber = models.CharField(max_length=25, verbose_name="TC Kimlik No / Vergi No",null=True,blank=True)
    adress = models.CharField(max_length=200, verbose_name="Adres",null=True,blank=True)
    tax = models.CharField(max_length=100, verbose_name="Vergi Dairesi",null=True,blank=True)
    mail1 = models.EmailField(max_length=100, verbose_name="E-mail 1",null=True,blank=True)
    mail2 = models.EmailField(max_length=100, verbose_name="E-mail 2",null=True,blank=True)
    phoneNumber1 = models.CharField(max_length=20, verbose_name="Telefon 1",null=True,blank=True)
    phoneNumber2 = models.CharField(max_length=20, verbose_name="Telefon 2",null=True,blank=True)
    IBAN = models.CharField(max_length=100, verbose_name="IBAN",null=True,blank=True)

    def __str__(self):
        return self.name


class Hammadde(models.Model):
    rawMaterialName = models.CharField(max_length=200, verbose_name="Hammadde Tipi")
    category=models.CharField(max_length=50,verbose_name="Mal Kategorisi",null=True,blank=True)

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
    note = models.TextField(verbose_name="Not", null=True, blank=True, max_length=180)
    odeme = models.CharField(max_length=100, verbose_name="Ödeme yapıldı mı?", choices=
    [('EVET', 'EVET'), ('HAYIR', 'HAYIR')])
    nakliyat = models.CharField(max_length=100, verbose_name="Taşıma", choices=
    [('PP', 'PP'), ('Ted', 'Ted')])
    faturaNo = models.TextField(verbose_name="Fatura No", null=True, blank=True)
    faturaTarihi = models.DateField(verbose_name="Fatura Tarihi", null=True, blank=True, )

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
    hurda = models.FloatField(verbose_name="Fire")
    birimFiyat = models.FloatField(verbose_name="Birim Fiyat")
    kantar = models.ForeignKey(Kantar, on_delete=models.DO_NOTHING, verbose_name="Kantar tartım numarası")
    odenecek = models.FloatField(verbose_name="Ödenen Tutar", blank=True, null=True)

    @property
    def ode(self):
        return (self.miktar - self.hurda) * self.birimFiyat

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

    def __str__(self):
        return self.name + " " + self.surname + " / " + self.companyName


class SonUrun(models.Model):
    urun = models.CharField(max_length=200, verbose_name="Ürün Tipi")

    def __str__(self):
        return self.urun


class Satis(models.Model):
    musteri = models.ForeignKey(musteri, on_delete=models.DO_NOTHING, verbose_name="Müşteri")
    miktar = models.FloatField(verbose_name="Miktar")
    urunTipi = models.ForeignKey(SonUrun, on_delete=models.DO_NOTHING, verbose_name="Ürün Tipi")
    birimFiyat = models.FloatField(verbose_name="Birim Fiyat")
    satisTarihi = models.DateTimeField(verbose_name="Satış Tarihi", default=datetime.now)
    faturaNo = models.TextField(verbose_name="Fatura No",)
    faturaTarihi = models.DateField(verbose_name="Fatura Tarihi",default=datetime.today)

    def __str__(self):
        return f'{str(self.id)} nolu satış : {str(self.miktar)}kg {str(self.urunTipi)}'
