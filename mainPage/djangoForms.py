from django import forms
from django.forms import ModelForm, NumberInput, DateTimeInput, Select, TextInput, Textarea,DateInput
from . import models


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
            'tedarikci': Select({"class": "form-control mb-3", "placeholder": 'Tedarikçi'}),
            'note': Textarea({'class': "form-control mb-3", "placeholder": "Not girin"}),
            'odeme': Select({'class': 'form-control mb-3', 'placeholder': 'Ödeme yapıldı mı?'}),
            'nakliyat': Select({'class': 'form-control mb-3', 'placeholder': 'Nakliyatı kim yaptı?'}),
        }


class MalzemeGirisForm(ModelForm):
    class Meta:
        model = models.MalzemeGiris
        fields = "__all__"


class MalAlimForm(ModelForm):
    class Meta:
        model = models.MalAlim
        fields = "__all__"
        exclude = ["kantar",'odenecek']
        widgets = {
            'mal': Select({"class": "form-control", }),
            'miktar': NumberInput({"class": "form-control field1 ", 'id': 'field1', }),
            'hurda': NumberInput({"class": "form-control field2 ", 'id': 'field2', }),
            'birimFiyat': NumberInput({"class": "form-control field3 ", 'id': 'field3', }),
            # 'odenecek': NumberInput({"class": "form-control field4 ", 'id': 'field4','placeholder':0},),
        }


class AlimKayitlarQueryForm(forms.Form):
    kantarNo = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': "Kantar No", "class": "form-control"}),
                                  required=False)
    tarih = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': "Tarih (Örn: >01.01.2023 )", "class": "form-control"}),
        required=False)
    tedarikci = forms.ModelChoiceField(label="Tedarikçi", queryset=models.Tedarikci.objects.all(),
                                       widget=forms.Select(attrs={'placeholder': "Tedarikçi", "class": "form-control"}),
                                       required=False)
    malTipi = forms.ModelChoiceField(label="Mal Tipi", queryset=models.Hammadde.objects.all(),
                                     widget=forms.Select(attrs={'placeholder': "Mal Tipi", "class": "form-control"}),
                                     required=False)
    odeme = forms.ChoiceField(label="Ödendi ?",
                              choices=(('EVET', 'EVET'), ('HAYIR', 'HAYIR'),("","---")),
                              widget=forms.Select(attrs={'placeholder': "Ödeme Yapıldı mı?", "class": "form-control"}),
                              required=False)

class FinalizeBuy(forms.Form):
    odenecek=forms.FloatField(label="",widget=forms.NumberInput(attrs={"class": "form-control sum-input"}))



class faturasizForm(ModelForm):
    class Meta:
        model=models.Kantar
        exclude = ["kantar3", 'kantar4','kantar4','kantar4']
        widgets = {
            'kantar1': NumberInput({"class": "form-control mb-3",'placeholder': 'Kantar1' }),
            'kantar2': NumberInput({"class": "form-control mb-3",'placeholder': 'Kantar2' }),
            'tedarikci': Select({"class": "form-control mb-3", "placeholder": 'Tedarikçi'}),
            'note': Textarea({'class': "form-control mb-3", "placeholder": "Not girin"}),
            'odeme': Select({'class': 'form-control mb-3', 'placeholder': 'Ödeme yapıldı mı?'}),
            'nakliyat': Select({'class': 'form-control mb-3', 'placeholder': 'Nakliyatı kim yaptı?'}),
            'faturaNo': TextInput({'class': "form-control mb-3", "placeholder": "Fatura No"}),
            'faturaTarihi':DateInput({'class': "form-control mb-3", "placeholder": "YYYY-AA-GG formatında"}),

        }


class SatisForm(ModelForm):
    class Meta:
        model = models.Satis
        fields = "__all__"
        widgets = {
            'musteri': Select({"class": "form-control", }),
            'miktar': NumberInput({"class": "form-control field1 ", }),
            'urunTipi': Select({"class": "form-control field2 ", }),
            'birimFiyat': NumberInput({"class": "form-control  ",}),
            'satisTarihi':DateTimeInput({"class": "form-control  ",}),
            'faturaNo':TextInput({"class": "form-control  ",}),
            'faturaTarihi':DateInput({"class": "form-control  ",})
        }