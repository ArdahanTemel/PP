from django import forms
from django.forms import ModelForm, NumberInput, DateTimeInput, Select, TextInput,Textarea
from . import models


# def getLatestentryNumber():
#     latestRecordId = models.Alimlar.objects.all().latest("alimKodu").alimKodu
#     # print(latestRecordId)
#     latestPlusOne = latestRecordId + 1
#     return latestPlusOne


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


# class BuyForm1(ModelForm):
#     class Meta:
#         model = models.Alimlar
#         fields = "__all__"
#         widgets = {
#             'alimKodu': NumberInput(
#                 {"class": "form-control m-3 ", "id": "form1"}),
#             'tedarikEden': Select({"class": "form-control m-3", 'id': "selection1"}),
#             'mal': Select({"class": "form-control m-3"}),
#             'miktar': NumberInput({"class": "form-control m-3 group-b", "id": "input1b"}),
#             'tarih': DateTimeInput({"class": "form-control m-3"}),
#             'birimFiyat': NumberInput({"class": "form-control m-3"}),
#             'alimKoduGenel': NumberInput({"class": "form-control m-3"}),
#
#         }
#
#
# class BuyForm2(ModelForm):
#     class Meta:
#         model = models.Alimlar
#         fields = "__all__"
#         widgets = {
#             'alimKodu': NumberInput({"class": "form-control m-3", "id": "form2"}),
#             'tedarikEden': Select({"class": "form-control m-3", 'id': "selection2"}),
#             'mal': Select({"class": "form-control m-3"}),
#             'miktar': NumberInput({"class": "form-control m-3 group-b", "id": "input2b"}),
#             'tarih': DateTimeInput({"class": "form-control m-3"}),
#             'birimFiyat': NumberInput({"class": "form-control m-3"}),
#             'alimKoduGenel': NumberInput({"class": "form-control m-3"}),
#
#         }
#
#
# class BuyForm3(ModelForm):
#     class Meta:
#         model = models.Alimlar
#         fields = "__all__"
#         widgets = {
#             'alimKodu': NumberInput({"class": "form-control m-3", "id": "form3"}),
#             'tedarikEden': Select({"class": "form-control m-3", "id": 'selection3'}),
#             'mal': Select({"class": "form-control m-3"}),
#             'miktar': NumberInput({"class": "form-control m-3 group-b", "id": "input3b"}),
#             'tarih': DateTimeInput({"class": "form-control m-3"}),
#             'birimFiyat': NumberInput({"class": "form-control m-3"}),
#             'alimKoduGenel': NumberInput({"class": "form-control m-3"}),
#
#         }
#
#
# class BuyForm4(ModelForm):
#     class Meta:
#         model = models.Alimlar
#         fields = "__all__"
#         widgets = {
#             'alimKodu': NumberInput({"class": "form-control m-3", "id": "form4"}),
#             'tedarikEden': Select({"class": "form-control m-3", "id": 'selection4'}),
#             'mal': Select({"class": "form-control m-3"}),
#             'miktar': NumberInput({"class": "form-control m-3 group-b", "id": "input4b"}),
#             'tarih': DateTimeInput({"class": "form-control m-3"}),
#             'birimFiyat': NumberInput({"class": "form-control m-3"}),
#             'alimKoduGenel': NumberInput({"class": "form-control m-3"}),
#
#         }
#
#
# class BuyForm5(ModelForm):
#     class Meta:
#         model = models.Alimlar
#         fields = "__all__"
#         widgets = {
#             'alimKodu': NumberInput({"class": "form-control m-3", "id": "form5"}),
#             'tedarikEden': Select({"class": "form-control m-3", "id": 'selection5'}),
#             'mal': Select({"class": "form-control m-3"}),
#             'miktar': NumberInput({"class": "form-control m-3 group-b", "id": "input5b"}),
#             'tarih': DateTimeInput({"class": "form-control m-3"}),
#             'birimFiyat': NumberInput({"class": "form-control m-3"}),
#             'alimKoduGenel': NumberInput({"class": "form-control m-3"}),
#
#         }
#
#
# class BuyForm1a(ModelForm):
#     class Meta:
#         model = models.Alimlar_Kirilim
#         fields = "__all__"
#         widgets = {
#             'alimKodu': TextInput({"class": "form-control m-3"}),
#             'tedarikEden': Select({"class": "form-control m-3", 'id': "selection1a"}),
#             'mal': Select({"class": "form-control m-3"}),
#             'miktar': NumberInput({"class": "form-control m-3"}),
#             'tarih': DateTimeInput({"class": "form-control m-3"}),
#             'birimFiyat': NumberInput({"class": "form-control m-3"}),
#             'alimKoduGenel': NumberInput({"class": "form-control m-3"}),
#
#         }
#
#
# class BuyForm1b(ModelForm):
#     class Meta:
#         model = models.Alimlar_Kirilim
#         fields = "__all__"
#         widgets = {
#             'alimKodu': TextInput({"class": "form-control m-3"}),
#             'tedarikEden': Select({"class": "form-control m-3", 'id': "selection1b"}),
#             'mal': Select({"class": "form-control m-3"}),
#             'miktar': NumberInput({"class": "form-control m-3"}),
#             'tarih': DateTimeInput({"class": "form-control m-3"}),
#             'birimFiyat': NumberInput({"class": "form-control m-3"}),
#             'alimKoduGenel': NumberInput({"class": "form-control m-3"}),
#
#         }
#
#
# class BuyForm1c(ModelForm):
#     class Meta:
#         model = models.Alimlar_Kirilim
#         fields = "__all__"
#         widgets = {
#             'alimKodu': TextInput({"class": "form-control m-3"}),
#             'tedarikEden': Select({"class": "form-control m-3", 'id': "selection1c"}),
#             'mal': Select({"class": "form-control m-3"}),
#             'miktar': NumberInput({"class": "form-control m-3"}),
#             'tarih': DateTimeInput({"class": "form-control m-3"}),
#             'birimFiyat': NumberInput({"class": "form-control m-3"}),
#             'alimKoduGenel': NumberInput({"class": "form-control m-3"}),
#
#         }
#
#
# class BuyForm2a(ModelForm):
#     class Meta:
#         model = models.Alimlar_Kirilim
#         fields = "__all__"
#         widgets = {
#             'alimKodu': TextInput({"class": "form-control m-3"}),
#             'tedarikEden': Select({"class": "form-control m-3", 'id': "selection2a"}),
#             'mal': Select({"class": "form-control m-3"}),
#             'miktar': NumberInput({"class": "form-control m-3"}),
#             'tarih': DateTimeInput({"class": "form-control m-3"}),
#             'birimFiyat': NumberInput({"class": "form-control m-3"}),
#             'alimKoduGenel': NumberInput({"class": "form-control m-3"}),
#
#         }
#
#
# class BuyForm2b(ModelForm):
#     class Meta:
#         model = models.Alimlar_Kirilim
#         fields = "__all__"
#         widgets = {
#             'alimKodu': TextInput({"class": "form-control m-3"}),
#             'tedarikEden': Select({"class": "form-control m-3", 'id': "selection2b"}),
#             'mal': Select({"class": "form-control m-3"}),
#             'miktar': NumberInput({"class": "form-control m-3"}),
#             'tarih': DateTimeInput({"class": "form-control m-3"}),
#             'birimFiyat': NumberInput({"class": "form-control m-3"}),
#             'alimKoduGenel': NumberInput({"class": "form-control m-3"}),
#
#         }
#
#
# class BuyForm2c(ModelForm):
#     class Meta:
#         model = models.Alimlar_Kirilim
#         fields = "__all__"
#         widgets = {
#             'alimKodu': TextInput({"class": "form-control m-3"}),
#             'tedarikEden': Select({"class": "form-control m-3", 'id': "selection2c"}),
#             'mal': Select({"class": "form-control m-3"}),
#             'miktar': NumberInput({"class": "form-control m-3"}),
#             'tarih': DateTimeInput({"class": "form-control m-3"}),
#             'birimFiyat': NumberInput({"class": "form-control m-3"}),
#             'alimKoduGenel': NumberInput({"class": "form-control m-3"}),
#         }
#
#
# class BuyForm3a(ModelForm):
#     class Meta:
#         model = models.Alimlar_Kirilim
#         fields = "__all__"
#         widgets = {
#             'alimKodu': TextInput({"class": "form-control m-3"}),
#             'tedarikEden': Select({"class": "form-control m-3", 'id': "selection3a"}),
#             'mal': Select({"class": "form-control m-3"}),
#             'miktar': NumberInput({"class": "form-control m-3"}),
#             'tarih': DateTimeInput({"class": "form-control m-3"}),
#             'birimFiyat': NumberInput({"class": "form-control m-3"}),
#             'alimKoduGenel': NumberInput({"class": "form-control m-3"}),
#
#         }
#
#
# class BuyForm3b(ModelForm):
#     class Meta:
#         model = models.Alimlar_Kirilim
#         fields = "__all__"
#         widgets = {
#             'alimKodu': TextInput({"class": "form-control m-3"}),
#             'tedarikEden': Select({"class": "form-control m-3", 'id': "selection3b"}),
#             'mal': Select({"class": "form-control m-3"}),
#             'miktar': NumberInput({"class": "form-control m-3"}),
#             'tarih': DateTimeInput({"class": "form-control m-3"}),
#             'birimFiyat': NumberInput({"class": "form-control m-3"}),
#             'alimKoduGenel': NumberInput({"class": "form-control m-3"}),
#
#         }
#
#
# class BuyForm3c(ModelForm):
#     class Meta:
#         model = models.Alimlar_Kirilim
#         fields = "__all__"
#         widgets = {
#             'alimKodu': TextInput({"class": "form-control m-3"}),
#             'tedarikEden': Select({"class": "form-control m-3", 'id': "selection3c"}),
#             'mal': Select({"class": "form-control m-3"}),
#             'miktar': NumberInput({"class": "form-control m-3"}),
#             'tarih': DateTimeInput({"class": "form-control m-3"}),
#             'birimFiyat': NumberInput({"class": "form-control m-3"}),
#             'alimKoduGenel': NumberInput({"class": "form-control m-3"}),
#
#         }
#
#
# class BuyForm4a(ModelForm):
#     class Meta:
#         model = models.Alimlar_Kirilim
#         fields = "__all__"
#         widgets = {
#             'alimKodu': TextInput({"class": "form-control m-3"}),
#             'tedarikEden': Select({"class": "form-control m-3", 'id': "selection4a"}),
#             'mal': Select({"class": "form-control m-3"}),
#             'miktar': NumberInput({"class": "form-control m-3"}),
#             'tarih': DateTimeInput({"class": "form-control m-3"}),
#             'birimFiyat': NumberInput({"class": "form-control m-3"}),
#             'alimKoduGenel': NumberInput({"class": "form-control m-3"}),
#
#         }
#
#
# class BuyForm4b(ModelForm):
#     class Meta:
#         model = models.Alimlar_Kirilim
#         fields = "__all__"
#         widgets = {
#             'alimKodu': TextInput({"class": "form-control m-3"}),
#             'tedarikEden': Select({"class": "form-control m-3", 'id': "selection4b"}),
#             'mal': Select({"class": "form-control m-3"}),
#             'miktar': NumberInput({"class": "form-control m-3"}),
#             'tarih': DateTimeInput({"class": "form-control m-3"}),
#             'birimFiyat': NumberInput({"class": "form-control m-3"}),
#             'alimKoduGenel': NumberInput({"class": "form-control m-3"}),
#
#         }
#
#
# class BuyForm4c(ModelForm):
#     class Meta:
#         model = models.Alimlar_Kirilim
#         fields = "__all__"
#         widgets = {
#             'alimKodu': TextInput({"class": "form-control m-3"}),
#             'tedarikEden': Select({"class": "form-control m-3", 'id': "selection4c"}),
#             'mal': Select({"class": "form-control m-3"}),
#             'miktar': NumberInput({"class": "form-control m-3"}),
#             'tarih': DateTimeInput({"class": "form-control m-3"}),
#             'birimFiyat': NumberInput({"class": "form-control m-3"}),
#             'alimKoduGenel': NumberInput({"class": "form-control m-3"}),
#
#         }
#
#
# class BuyForm5a(ModelForm):
#     class Meta:
#         model = models.Alimlar_Kirilim
#         fields = "__all__"
#         widgets = {
#             'alimKodu': TextInput({"class": "form-control m-3"}),
#             'tedarikEden': Select({"class": "form-control m-3", 'id': "selection5a"}),
#             'mal': Select({"class": "form-control m-3"}),
#             'miktar': NumberInput({"class": "form-control m-3"}),
#             'tarih': DateTimeInput({"class": "form-control m-3"}),
#             'birimFiyat': NumberInput({"class": "form-control m-3"}),
#             'alimKoduGenel': NumberInput({"class": "form-control m-3"}),
#
#         }
#
#
# class BuyForm5b(ModelForm):
#     class Meta:
#         model = models.Alimlar_Kirilim
#         fields = "__all__"
#         widgets = {
#             'alimKodu': TextInput({"class": "form-control m-3"}),
#             'tedarikEden': Select({"class": "form-control m-3", 'id': "selection5b"}),
#             'mal': Select({"class": "form-control m-3"}),
#             'miktar': NumberInput({"class": "form-control m-3"}),
#             'tarih': DateTimeInput({"class": "form-control m-3"}),
#             'birimFiyat': NumberInput({"class": "form-control m-3"}),
#             'alimKoduGenel': NumberInput({"class": "form-control m-3"}),
#
#         }
#
#
# class BuyForm5c(ModelForm):
#     class Meta:
#         model = models.Alimlar_Kirilim
#         fields = "__all__"
#         widgets = {
#             'alimKodu': TextInput({"class": "form-control m-3"}),
#             'tedarikEden': Select({"class": "form-control m-3", 'id': "selection5c"}),
#             'mal': Select({"class": "form-control m-3"}),
#             'miktar': NumberInput({"class": "form-control m-3"}),
#             'tarih': DateTimeInput({"class": "form-control m-3"}),
#             'birimFiyat': NumberInput({"class": "form-control m-3"}),
#             'alimKoduGenel': NumberInput({"class": "form-control m-3"}),
#
#         }
#
#
# class MalGirisForm(ModelForm):
#     class Meta:
#         model = models.MalGiris
#         fields = "__all__"
#
#         widgets = {
#             'alimKodu': TextInput({"class": "form-control ", "id": "form1"}),
#             'tedarikEden': Select({"class": "form-control ", 'id': "selection5c"}),
#             'tarih': DateTimeInput({"class": "form-control "}),
#
#             'mal1': Select({"class": "form-control "}),
#             'miktar1': NumberInput({"class": "form-control group-b"}),
#             'birimFiyat1': NumberInput({"class": "form-control "}),
#
#             'mal1a': Select({"class": "form-control "}),
#             'miktar1a': NumberInput({"class": "form-control "}),
#             'birimFiyat1a': NumberInput({"class": "form-control "}),
#
#             'mal1b': Select({"class": "form-control "}),
#             'miktar1b': NumberInput({"class": "form-control "}),
#             'birimFiyat1b': NumberInput({"class": "form-control "}),
#
#             'mal1c': Select({"class": "form-control "}),
#             'miktar1c': NumberInput({"class": "form-control "}),
#             'birimFiyat1c': NumberInput({"class": "form-control "}),
#
#             'mal2': Select({"class": "form-control "}),
#             'miktar2': NumberInput({"class": "form-control group-b"}),
#             'birimFiyat2': NumberInput({"class": "form-control "}),
#
#             'mal2a': Select({"class": "form-control "}),
#             'miktar2a': NumberInput({"class": "form-control "}),
#             'birimFiyat2a': NumberInput({"class": "form-control "}),
#
#             'mal2b': Select({"class": "form-control "}),
#             'miktar2b': NumberInput({"class": "form-control "}),
#             'birimFiyat2b': NumberInput({"class": "form-control "}),
#
#             'mal2c': Select({"class": "form-control "}),
#             'miktar2c': NumberInput({"class": "form-control "}),
#             'birimFiyat2c': NumberInput({"class": "form-control "}),
#
#             'mal3': Select({"class": "form-control "}),
#             'miktar3': NumberInput({"class": "form-control group-b"}),
#             'birimFiyat3': NumberInput({"class": "form-control "}),
#
#             'mal3a': Select({"class": "form-control "}),
#             'miktar3a': NumberInput({"class": "form-control "}),
#             'birimFiyat3a': NumberInput({"class": "form-control "}),
#
#             'mal3b': Select({"class": "form-control "}),
#             'miktar3b': NumberInput({"class": "form-control "}),
#             'birimFiyat3b': NumberInput({"class": "form-control "}),
#
#             'mal3c': Select({"class": "form-control "}),
#             'miktar3c': NumberInput({"class": "form-control "}),
#             'birimFiyat3c': NumberInput({"class": "form-control "}),
#
#             'mal4': Select({"class": "form-control "}),
#             'miktar4': NumberInput({"class": "form-control group-b"}),
#             'birimFiyat4': NumberInput({"class": "form-control "}),
#
#             'mal4a': Select({"class": "form-control "}),
#             'miktar4a': NumberInput({"class": "form-control "}),
#             'birimFiyat4a': NumberInput({"class": "form-control "}),
#
#             'mal4b': Select({"class": "form-control "}),
#             'miktar4b': NumberInput({"class": "form-control "}),
#             'birimFiyat4b': NumberInput({"class": "form-control "}),
#
#             'mal4c': Select({"class": "form-control "}),
#             'miktar4c': NumberInput({"class": "form-control "}),
#             'birimFiyat4c': NumberInput({"class": "form-control "}),
#
#             'mal5': Select({"class": "form-control "}),
#             'miktar5': NumberInput({"class": "form-control group-b"}),
#             'birimFiyat5': NumberInput({"class": "form-control "}),
#
#             'mal5a': Select({"class": "form-control "}),
#             'miktar5a': NumberInput({"class": "form-control "}),
#             'birimFiyat5a': NumberInput({"class": "form-control "}),
#
#             'mal5b': Select({"class": "form-control "}),
#             'miktar5b': NumberInput({"class": "form-control "}),
#             'birimFiyat5b': NumberInput({"class": "form-control "}),
#
#             'mal5c': Select({"class": "form-control "}),
#             'miktar5c': NumberInput({"class": "form-control "}),
#             'birimFiyat5c': NumberInput({"class": "form-control "}),
#
#         }


class kantarForm(ModelForm):
    class Meta:
        model = models.Kantar
        fields = "__all__"
        widgets = {
            'giris': NumberInput({'class': "hidden2", "id": "myInput"}),
            'kantar1': NumberInput({"class": "form-control mb-3 ", "id": "input1", 'placeholder': 'Kantar1'}),
            'kantar2': NumberInput({"class": "form-control mb-3 ", "id": "input2", 'placeholder': 'Kantar2'}),
            'kantar3': NumberInput({"class": "form-control mb-3 ", "id": "input3", 'placeholder': 'Kantar3'}),
            'kantar4': NumberInput({"class": "hidden form-control mb-3 ", "id": "input4", 'placeholder': 'Kantar4'}),
            'kantar5': NumberInput({"class": "hidden form-control mb-3 ", "id": "input5", 'placeholder': 'Kantar5'}),
            'kantar6': NumberInput({"class": "hidden form-control mb-3 ", "id": "input6", 'placeholder': 'Kantar6'}),
            'tarih': DateTimeInput({"class": " form-control mb-3 "}),
            'tedarikci': Select({"class": "form-control mb-3","placeholder": 'Tedarikçi' }),
            'note':Textarea({'class':"form-control mb-3","placeholder":"Not girin"})
        }





class MalzemeGirisForm(ModelForm):
    class Meta:
        model = models.MalzemeGiris
        fields = "__all__"


class MalAlimForm(ModelForm):
    class Meta:
        model = models.MalAlim
        fields = "__all__"
        exclude = ["kantar"]
        widgets={
            'mal': Select({"class": "form-control", }),
            'miktar': NumberInput({"class":"form-control ", }),
            'hurda': NumberInput({"class": "form-control ", }),
            'birimFiyat': NumberInput({"class": "form-control ", }),

        }