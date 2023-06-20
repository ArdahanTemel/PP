from django import forms
from django.forms import ModelForm, NumberInput, DateTimeInput, Select, TextInput
from . import models


def getLatestentryNumber():
    latestRecordId = models.Alimlar.objects.all().latest("alimKodu").alimKodu
    # print(latestRecordId)
    latestPlusOne = latestRecordId + 1
    return latestPlusOne


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label="Kullanıcı Adı : ", widget=forms.
                               TextInput(attrs={'type': "text",
                                                'class': "form-control",
                                                'id': "exampleInputEmail1",
                                                'aria-describedby': "emailHelp"
                                                }
                                         )
                               )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type': "password",
                                                                 'class': "form-control",
                                                                 'id': "exampleInputPassword1"
                                                                 }), label="Şifre : ")


class BuyForm1(ModelForm):
    class Meta:
        model = models.Alimlar
        fields = "__all__"
        widgets = {
            'alimKodu': NumberInput(
                {"class": "form-control m-3 ", "id": "form1"}),
            'tedarikEden': Select({"class": "form-control m-3", 'id': "selection1"}),
            'mal': Select({"class": "form-control m-3"}),
            'miktar': NumberInput({"class": "form-control m-3 group-b", "id": "input1b"}),
            'tarih': DateTimeInput({"class": "form-control m-3"}),
            'birimFiyat': NumberInput({"class": "form-control m-3"}),
            'alimKoduGenel': NumberInput({"class": "form-control m-3"}),

        }


class BuyForm2(ModelForm):
    class Meta:
        model = models.Alimlar
        fields = "__all__"
        widgets = {
            'alimKodu': NumberInput({"class": "form-control m-3","id": "form2" }),
            'tedarikEden': Select({"class": "form-control m-3", 'id': "selection2"}),
            'mal': Select({"class": "form-control m-3"}),
            'miktar': NumberInput({"class": "form-control m-3 group-b", "id": "input2b"}),
            'tarih': DateTimeInput({"class": "form-control m-3"}),
            'birimFiyat': NumberInput({"class": "form-control m-3"}),
            'alimKoduGenel': NumberInput({"class": "form-control m-3"}),

        }


class BuyForm3(ModelForm):
    class Meta:
        model = models.Alimlar
        fields = "__all__"
        widgets = {
            'alimKodu': NumberInput({"class": "form-control m-3", "id": "form3"}),
            'tedarikEden': Select({"class": "form-control m-3", "id": 'selection3'}),
            'mal': Select({"class": "form-control m-3"}),
            'miktar': NumberInput({"class": "form-control m-3 group-b", "id": "input3b"}),
            'tarih': DateTimeInput({"class": "form-control m-3"}),
            'birimFiyat': NumberInput({"class": "form-control m-3"}),
            'alimKoduGenel': NumberInput({"class": "form-control m-3"}),

        }


class BuyForm4(ModelForm):
    class Meta:
        model = models.Alimlar
        fields = "__all__"
        widgets = {
            'alimKodu': NumberInput({"class": "form-control m-3","id": "form4"}),
            'tedarikEden': Select({"class": "form-control m-3", "id": 'selection4'}),
            'mal': Select({"class": "form-control m-3"}),
            'miktar': NumberInput({"class": "form-control m-3 group-b", "id": "input4b"}),
            'tarih': DateTimeInput({"class": "form-control m-3"}),
            'birimFiyat': NumberInput({"class": "form-control m-3"}),
            'alimKoduGenel': NumberInput({"class": "form-control m-3"}),

        }


class BuyForm5(ModelForm):
    class Meta:
        model = models.Alimlar
        fields = "__all__"
        widgets = {
            'alimKodu': NumberInput({"class": "form-control m-3","id": "form5"}),
            'tedarikEden': Select({"class": "form-control m-3","id": 'selection5'}),
            'mal': Select({"class": "form-control m-3"}),
            'miktar': NumberInput({"class": "form-control m-3 group-b", "id": "input5b"}),
            'tarih': DateTimeInput({"class": "form-control m-3"}),
            'birimFiyat': NumberInput({"class": "form-control m-3"}),
            'alimKoduGenel': NumberInput({"class": "form-control m-3"}),

        }


class BuyForm1a(ModelForm):
    class Meta:
        model = models.Alimlar_Kirilim
        fields = "__all__"
        widgets = {
            'alimKodu': TextInput({"class": "form-control m-3"}),
            'tedarikEden': Select({"class": "form-control m-3",'id': "selection1a"}),
            'mal': Select({"class": "form-control m-3"}),
            'miktar': NumberInput({"class": "form-control m-3"}),
            'tarih': DateTimeInput({"class": "form-control m-3"}),
            'birimFiyat': NumberInput({"class": "form-control m-3"}),
            'alimKoduGenel': NumberInput({"class": "form-control m-3"}),

        }


class BuyForm1b(ModelForm):
    class Meta:
        model = models.Alimlar_Kirilim
        fields = "__all__"
        widgets = {
            'alimKodu': TextInput({"class": "form-control m-3"}),
            'tedarikEden': Select({"class": "form-control m-3",'id': "selection1b"}),
            'mal': Select({"class": "form-control m-3"}),
            'miktar': NumberInput({"class": "form-control m-3"}),
            'tarih': DateTimeInput({"class": "form-control m-3"}),
            'birimFiyat': NumberInput({"class": "form-control m-3"}),
            'alimKoduGenel': NumberInput({"class": "form-control m-3"}),

        }


class BuyForm1c(ModelForm):
    class Meta:
        model = models.Alimlar_Kirilim
        fields = "__all__"
        widgets = {
            'alimKodu': TextInput({"class": "form-control m-3"}),
            'tedarikEden': Select({"class": "form-control m-3",'id': "selection1c"}),
            'mal': Select({"class": "form-control m-3"}),
            'miktar': NumberInput({"class": "form-control m-3"}),
            'tarih': DateTimeInput({"class": "form-control m-3"}),
            'birimFiyat': NumberInput({"class": "form-control m-3"}),
            'alimKoduGenel': NumberInput({"class": "form-control m-3"}),

        }


class BuyForm2a(ModelForm):
    class Meta:
        model = models.Alimlar_Kirilim
        fields = "__all__"
        widgets = {
            'alimKodu': TextInput({"class": "form-control m-3"}),
            'tedarikEden': Select({"class": "form-control m-3",'id': "selection2a"}),
            'mal': Select({"class": "form-control m-3"}),
            'miktar': NumberInput({"class": "form-control m-3"}),
            'tarih': DateTimeInput({"class": "form-control m-3"}),
            'birimFiyat': NumberInput({"class": "form-control m-3"}),
            'alimKoduGenel': NumberInput({"class": "form-control m-3"}),

        }


class BuyForm2b(ModelForm):
    class Meta:
        model = models.Alimlar_Kirilim
        fields = "__all__"
        widgets = {
            'alimKodu': TextInput({"class": "form-control m-3"}),
            'tedarikEden': Select({"class": "form-control m-3",'id': "selection2b"}),
            'mal': Select({"class": "form-control m-3"}),
            'miktar': NumberInput({"class": "form-control m-3"}),
            'tarih': DateTimeInput({"class": "form-control m-3"}),
            'birimFiyat': NumberInput({"class": "form-control m-3"}),
            'alimKoduGenel': NumberInput({"class": "form-control m-3"}),

        }


class BuyForm2c(ModelForm):
    class Meta:
        model = models.Alimlar_Kirilim
        fields = "__all__"
        widgets = {
            'alimKodu': TextInput({"class": "form-control m-3"}),
            'tedarikEden': Select({"class": "form-control m-3",'id': "selection2c"}),
            'mal': Select({"class": "form-control m-3"}),
            'miktar': NumberInput({"class": "form-control m-3"}),
            'tarih': DateTimeInput({"class": "form-control m-3"}),
            'birimFiyat': NumberInput({"class": "form-control m-3"}),
            'alimKoduGenel': NumberInput({"class": "form-control m-3"}),
        }


class BuyForm3a(ModelForm):
    class Meta:
        model = models.Alimlar_Kirilim
        fields = "__all__"
        widgets = {
            'alimKodu': TextInput({"class": "form-control m-3"}),
            'tedarikEden': Select({"class": "form-control m-3",'id': "selection3a"}),
            'mal': Select({"class": "form-control m-3"}),
            'miktar': NumberInput({"class": "form-control m-3"}),
            'tarih': DateTimeInput({"class": "form-control m-3"}),
            'birimFiyat': NumberInput({"class": "form-control m-3"}),
            'alimKoduGenel': NumberInput({"class": "form-control m-3"}),

        }


class BuyForm3b(ModelForm):
    class Meta:
        model = models.Alimlar_Kirilim
        fields = "__all__"
        widgets = {
            'alimKodu': TextInput({"class": "form-control m-3"}),
            'tedarikEden': Select({"class": "form-control m-3",'id': "selection3b"}),
            'mal': Select({"class": "form-control m-3"}),
            'miktar': NumberInput({"class": "form-control m-3"}),
            'tarih': DateTimeInput({"class": "form-control m-3"}),
            'birimFiyat': NumberInput({"class": "form-control m-3"}),
            'alimKoduGenel': NumberInput({"class": "form-control m-3"}),

        }


class BuyForm3c(ModelForm):
    class Meta:
        model = models.Alimlar_Kirilim
        fields = "__all__"
        widgets = {
            'alimKodu': TextInput({"class": "form-control m-3"}),
            'tedarikEden': Select({"class": "form-control m-3",'id': "selection3c"}),
            'mal': Select({"class": "form-control m-3"}),
            'miktar': NumberInput({"class": "form-control m-3"}),
            'tarih': DateTimeInput({"class": "form-control m-3"}),
            'birimFiyat': NumberInput({"class": "form-control m-3"}),
            'alimKoduGenel': NumberInput({"class": "form-control m-3"}),

        }


class BuyForm4a(ModelForm):
    class Meta:
        model = models.Alimlar_Kirilim
        fields = "__all__"
        widgets = {
            'alimKodu': TextInput({"class": "form-control m-3"}),
            'tedarikEden': Select({"class": "form-control m-3",'id': "selection4a"}),
            'mal': Select({"class": "form-control m-3"}),
            'miktar': NumberInput({"class": "form-control m-3"}),
            'tarih': DateTimeInput({"class": "form-control m-3"}),
            'birimFiyat': NumberInput({"class": "form-control m-3"}),
            'alimKoduGenel': NumberInput({"class": "form-control m-3"}),

        }


class BuyForm4b(ModelForm):
    class Meta:
        model = models.Alimlar_Kirilim
        fields = "__all__"
        widgets = {
            'alimKodu': TextInput({"class": "form-control m-3"}),
            'tedarikEden': Select({"class": "form-control m-3",'id': "selection4b"}),
            'mal': Select({"class": "form-control m-3"}),
            'miktar': NumberInput({"class": "form-control m-3"}),
            'tarih': DateTimeInput({"class": "form-control m-3"}),
            'birimFiyat': NumberInput({"class": "form-control m-3"}),
            'alimKoduGenel': NumberInput({"class": "form-control m-3"}),

        }


class BuyForm4c(ModelForm):
    class Meta:
        model = models.Alimlar_Kirilim
        fields = "__all__"
        widgets = {
            'alimKodu': TextInput({"class": "form-control m-3"}),
            'tedarikEden': Select({"class": "form-control m-3",'id': "selection4c"}),
            'mal': Select({"class": "form-control m-3"}),
            'miktar': NumberInput({"class": "form-control m-3"}),
            'tarih': DateTimeInput({"class": "form-control m-3"}),
            'birimFiyat': NumberInput({"class": "form-control m-3"}),
            'alimKoduGenel': NumberInput({"class": "form-control m-3"}),

        }


class BuyForm5a(ModelForm):
    class Meta:
        model = models.Alimlar_Kirilim
        fields = "__all__"
        widgets = {
            'alimKodu': TextInput({"class": "form-control m-3"}),
            'tedarikEden': Select({"class": "form-control m-3",'id': "selection5a"}),
            'mal': Select({"class": "form-control m-3"}),
            'miktar': NumberInput({"class": "form-control m-3"}),
            'tarih': DateTimeInput({"class": "form-control m-3"}),
            'birimFiyat': NumberInput({"class": "form-control m-3"}),
            'alimKoduGenel': NumberInput({"class": "form-control m-3"}),

        }


class BuyForm5b(ModelForm):
    class Meta:
        model = models.Alimlar_Kirilim
        fields = "__all__"
        widgets = {
            'alimKodu': TextInput({"class": "form-control m-3"}),
            'tedarikEden': Select({"class": "form-control m-3",'id': "selection5b"}),
            'mal': Select({"class": "form-control m-3"}),
            'miktar': NumberInput({"class": "form-control m-3"}),
            'tarih': DateTimeInput({"class": "form-control m-3"}),
            'birimFiyat': NumberInput({"class": "form-control m-3"}),
            'alimKoduGenel': NumberInput({"class": "form-control m-3"}),

        }


class BuyForm5c(ModelForm):
    class Meta:
        model = models.Alimlar_Kirilim
        fields = "__all__"
        widgets = {
            'alimKodu': TextInput({"class": "form-control m-3"}),
            'tedarikEden': Select({"class": "form-control m-3",'id': "selection5c"}),
            'mal': Select({"class": "form-control m-3"}),
            'miktar': NumberInput({"class": "form-control m-3"}),
            'tarih': DateTimeInput({"class": "form-control m-3"}),
            'birimFiyat': NumberInput({"class": "form-control m-3"}),
            'alimKoduGenel': NumberInput({"class": "form-control m-3"}),

        }
