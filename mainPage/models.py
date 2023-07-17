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






# class Alimlar(models.Model):
#     alimKodu = models.IntegerField(primary_key=True, verbose_name="ID")
#     tedarikEden = models.ForeignKey(Tedarikci, on_delete=models.DO_NOTHING, verbose_name="Tedarikçi")
#     mal = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü")
#     miktar = models.FloatField(verbose_name="Ağırlık (kg)")
#     tarih = models.DateTimeField(verbose_name="Tarih", default=datetime.now)
#     birimFiyat = models.FloatField(verbose_name="Birim Fiyat")
#     alimKoduGenel = models.IntegerField(verbose_name="Alım Kodu")
#
#     def __str__(self):
#         return str(self.tarih) + "-" + str(self.miktar) + "-" + str(self.tedarikEden) + "-" + str(
#             self.alimKodu) + "-" + str(self.alimKoduGenel)
#
#
# class Alimlar_Kirilim(models.Model):
#     alimKodu = models.CharField(primary_key=True, verbose_name="ID", max_length=100)
#     tedarikEden = models.ForeignKey(Tedarikci, on_delete=models.DO_NOTHING, verbose_name="Tedarikçi")
#     mal = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü")
#     miktar = models.FloatField(verbose_name="Ağırlık (kg)")
#     tarih = models.DateTimeField(verbose_name="Tarih", default=datetime.now)
#     birimFiyat = models.FloatField(verbose_name="Birim Fiyat")
#     alimKoduGenel = models.IntegerField(verbose_name="Alım Kodu")
#
#     def __str__(self):
#         return str(self.tarih) + "-" + str(self.miktar) + "-" + str(self.tedarikEden)


# class MalGiris(models.Model):
#     alimKodu = models.IntegerField(primary_key=True, verbose_name="ID")
#     tedarikEden = models.ForeignKey(Tedarikci, on_delete=models.DO_NOTHING, verbose_name="Tedarikçi")
#     tarih = models.DateTimeField(verbose_name="Tarih", default=datetime.now)
#
#     mal1 = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü - 1",
#                              related_name="mal1")
#     miktar1 = models.FloatField(verbose_name="Ağırlık - 1")
#     birimFiyat1 = models.FloatField(verbose_name="Birim Fiyat - 1")
#
#     mal1a = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü - 1a",
#                               related_name="mal11a",
#                               blank=True, null=True)
#     miktar1a = models.FloatField(verbose_name="Ağırlık - 1a", blank=True, null=True)
#     birimFiyat1a = models.FloatField(verbose_name="Birim Fiyat - 1a", blank=True, null=True)
#
#     mal1b = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü - 1b",
#                               related_name="mal11b",
#                               blank=True, null=True)
#     miktar1b = models.FloatField(verbose_name="Ağırlık - 1b", blank=True, null=True)
#     birimFiyat1b = models.FloatField(verbose_name="Birim Fiyat - 1b", blank=True, null=True)
#
#     mal1c = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü - 1c",
#                               related_name="mal11c",
#                               blank=True, null=True)
#     miktar1c = models.FloatField(verbose_name="Ağırlık - 1c", blank=True, null=True)
#     birimFiyat1c = models.FloatField(verbose_name="Birim Fiyat - 1c", blank=True, null=True)
#
#     mal2 = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü - 2",
#                              related_name="mal12",
#                              blank=True, null=True)
#     miktar2 = models.FloatField(verbose_name="Ağırlık - 2", blank=True, null=True)
#     birimFiyat2 = models.FloatField(verbose_name="Birim Fiyat - 2", blank=True, null=True)
#
#     mal2a = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü - 2a",
#                               related_name="mal12a",
#                               blank=True, null=True)
#     miktar2a = models.FloatField(verbose_name="Ağırlık - 2a", blank=True, null=True)
#     birimFiyat2a = models.FloatField(verbose_name="Birim Fiyat - 2a", blank=True, null=True)
#
#     mal2b = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü - 2b",
#                               related_name="mal12b",
#                               blank=True, null=True)
#     miktar2b = models.FloatField(verbose_name="Ağırlık - 2b", blank=True, null=True)
#     birimFiyat2b = models.FloatField(verbose_name="Birim Fiyat - 2b", blank=True, null=True)
#
#     mal2c = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü - 2c",
#                               related_name="mal12c",
#                               blank=True, null=True)
#     miktar2c = models.FloatField(verbose_name="Ağırlık - 2c", blank=True, null=True)
#     birimFiyat2c = models.FloatField(verbose_name="Birim Fiyat - 2c", blank=True, null=True)
#
#     mal3 = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü - 3",
#                              related_name="mal13",
#                              blank=True, null=True)
#     miktar3 = models.FloatField(verbose_name="Ağırlık - 3", blank=True, null=True)
#     birimFiyat3 = models.FloatField(verbose_name="Birim Fiyat - 3", blank=True, null=True)
#
#     mal3a = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü - 3a",
#                               related_name="mal13a",
#                               blank=True, null=True)
#     miktar3a = models.FloatField(verbose_name="Ağırlık - 3a", blank=True, null=True)
#     birimFiyat3a = models.FloatField(verbose_name="Birim Fiyat - 3a", blank=True, null=True)
#
#     mal3b = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü - 3b",
#                               related_name="mal13b",
#                               blank=True, null=True)
#     miktar3b = models.FloatField(verbose_name="Ağırlık - 3b", blank=True, null=True)
#     birimFiyat3b = models.FloatField(verbose_name="Birim Fiyat - 3b", blank=True, null=True)
#
#     mal3c = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü - 3c",
#                               related_name="mal13c",
#                               blank=True, null=True)
#     miktar3c = models.FloatField(verbose_name="Ağırlık - 3c", blank=True, null=True)
#     birimFiyat3c = models.FloatField(verbose_name="Birim Fiyat - 3c", blank=True, null=True)
#
#     mal4 = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü - 4",
#                              related_name="mal14",
#                              blank=True, null=True)
#     miktar4 = models.FloatField(verbose_name="Ağırlık - 4", blank=True, null=True)
#     birimFiyat4 = models.FloatField(verbose_name="Birim Fiyat - 4", blank=True, null=True)
#
#     mal4a = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü - 4a",
#                               related_name="mal14a",
#                               blank=True, null=True)
#     miktar4a = models.FloatField(verbose_name="Ağırlık - 4a", blank=True, null=True)
#     birimFiyat4a = models.FloatField(verbose_name="Birim Fiyat - 4a", blank=True, null=True)
#
#     mal4b = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü - 4b",
#                               related_name="mal14b",
#                               blank=True, null=True)
#     miktar4b = models.FloatField(verbose_name="Ağırlık - 4b", blank=True, null=True)
#     birimFiyat4b = models.FloatField(verbose_name="Birim Fiyat - 4b", blank=True, null=True)
#
#     mal4c = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü - 4c",
#                               related_name="mal14c",
#                               blank=True, null=True)
#     miktar4c = models.FloatField(verbose_name="Ağırlık - 4c", blank=True, null=True)
#     birimFiyat4c = models.FloatField(verbose_name="Birim Fiyat - 4c", blank=True, null=True)
#
#     mal5 = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü - 5",
#                              related_name="mal15",
#                              blank=True, null=True)
#     miktar5 = models.FloatField(verbose_name="Ağırlık - 5", blank=True, null=True)
#     birimFiyat5 = models.FloatField(verbose_name="Birim Fiyat - 5", blank=True, null=True)
#
#     mal5a = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü - 5a",
#                               related_name="mal15a",
#                               blank=True, null=True)
#     miktar5a = models.FloatField(verbose_name="Ağırlık - 5a", blank=True, null=True)
#     birimFiyat5a = models.FloatField(verbose_name="Birim Fiyat - 5a", blank=True, null=True)
#
#     mal5b = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü - 5b",
#                               related_name="mal15b",
#                               blank=True, null=True)
#     miktar5b = models.FloatField(verbose_name="Ağırlık - 5b", blank=True, null=True)
#     birimFiyat5b = models.FloatField(verbose_name="Birim Fiyat - 5b", blank=True, null=True)
#
#     mal5c = models.ForeignKey(Hammadde, on_delete=models.DO_NOTHING, verbose_name="Malzeme Türü - 5c",
#                               related_name="mal15c",
#                               blank=True, null=True)
#     miktar5c = models.FloatField(verbose_name="Ağırlık - 5c", blank=True, null=True)
#     birimFiyat5c = models.FloatField(verbose_name="Birim Fiyat - 5c", blank=True, null=True)
#
#     def __str__(self):
#         return str(self.alimKodu) + "-" + str(self.tarih) + "-" + str(self.tedarikEden)


class Kantar(models.Model):
    kantar1 = models.FloatField(verbose_name="Kantar 1")
    kantar2 = models.FloatField(verbose_name="Kantar 2")
    kantar3 = models.FloatField(verbose_name="Kantar 3", null=True, blank=True)
    kantar4 = models.FloatField(verbose_name="Kantar 4", null=True, blank=True)
    kantar5 = models.FloatField(verbose_name="Kantar 5", null=True, blank=True)
    kantar6 = models.FloatField(verbose_name="Kantar 6", null=True, blank=True)
    tarih = models.DateTimeField(verbose_name="Tarih", default=datetime.now, blank=True, null=True)
    tedarikci = models.ForeignKey(Tedarikci, on_delete=models.DO_NOTHING, verbose_name="Tedarikçi")
    note=models.TextField(verbose_name="Not",null=True,blank=True)

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
