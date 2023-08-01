from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from . import djangoForms, models
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import djangoForms, models, helperFunctions
import time
from django.db.models import Q
from django.http import QueryDict
from django.urls import reverse
# from fpdf import FPDF
import os
from datetime import datetime


# def showPdf():
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font('Arial', 'B', 16)
#     pdf.cell(200, 10, txt="aaaaaaa")
#     pdfFile = "output.pdf"
#     pdf.output(pdfFile)
#     return pdfFile


def mainPageView(request):
    if request.user.is_authenticated:
        context = {}
        if request.method == "GET":
            kantarForm = djangoForms.kantarForm()
            context['kantarForm'] = kantarForm
            context['now'] = helperFunctions.datetime_to_int()
            context['buyQuery'] = getLastMalAlimRecords(30)

            return render(request, "mainPage/mainPage.html", context=context)

        elif request.method == "POST":
            kantarForm = djangoForms.kantarForm(request.POST)

            # data_copy.pop('giris', None)
            #
            #         # Update the form's data with the modified copy
            if kantarForm.is_valid():

                instance = kantarForm.save()

                # Generate the redirect URL with the model ID
                redirect_url = reverse('buy', kwargs={'id': instance.id})

                return redirect(redirect_url)


            else:
                print("Valid Değil")
                print(request.POST)
                context['kantarForm'] = kantarForm
                return render(request, "mainPage/mainPage.html", context=context)

        # print(request.user.username)

        # return render(request, "mainPage/mainPage.html",context=context)






    else:
        return redirect("/login")


def logoutView(request):
    logout(request)
    return redirect("/login")


def loginView(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # print("Login Başarılı")
            # messages.success(request, "Giriş başarılı")
            return redirect("../")
        else:
            print("login başarısız")
            messages.error(request, "Yanlış Şifre / Kullanıcı Adı ")

            return redirect("login")
    elif request.method == "GET":

        return render(request, "mainPage/login.html", context={"LoginForm": djangoForms.LoginForm})


def getLastMalAlimRecords(n):
    kantarlar = models.Kantar.objects.all().order_by('-tarih')[1:n]
    query = {}
    for kantar in kantarlar:
        query[str(kantar)] = (kantar, models.MalAlim.objects.filter(kantar=kantar.id))
    # for i in query:
    #     print(i, "*********", query[i])
    #     print("-------")
    return query


def buy1(request, id):
    if request.method == "POST":
        # print(dict(request.POST))
        submittedForms = []

        def getDataFromForms(requestDict):
            for i in range(len(requestDict['mal'])):
                submittedForms.append(
                    models.MalAlim(mal=models.Hammadde.objects.get(id=int(requestDict['mal'][i])),
                                   miktar=float(requestDict['miktar'][i]),
                                   hurda=float(requestDict['hurda'][i]),
                                   birimFiyat=float(requestDict['birimFiyat'][i]),
                                   kantar=models.Kantar.objects.get(id=int(id)),
                                   )
                )
            return submittedForms

        for alim in getDataFromForms(dict(request.POST)):
            alim.save()

        # pdf_file=showPdf()
        # response=HttpResponse(open(pdf_file,'rb').read(),content_type='application/pdf')
        # response['Content-Disposition']='inline;filename="output.pdf'
        # os.remove(pdf_file)
        # return response
        return redirect('mainPage')

    if request.method == "GET":
        kantar = models.Kantar.objects.get(id=id)

        def getKantarAmount():
            if kantar.kantar6 is not None:
                malAdedi = 5
            elif kantar.kantar5 is not None:
                malAdedi = 4
            elif kantar.kantar4 is not None:
                malAdedi = 3
            elif kantar.kantar3 is not None:
                malAdedi = 2
            elif kantar.kantar2 is not None:
                malAdedi = 1
            # print(malAdedi)
            return malAdedi

        def getMaterialWeights():
            weights = {}
            if getKantarAmount() == 5:
                weights['w5'] = kantar.kantar5 - kantar.kantar6
                weights['w4'] = kantar.kantar4 - kantar.kantar5
                weights['w3'] = kantar.kantar3 - kantar.kantar4
                weights['w2'] = kantar.kantar2 - kantar.kantar3
                weights['w1'] = kantar.kantar1 - kantar.kantar2
            elif getKantarAmount() == 4:
                weights['w4'] = kantar.kantar4 - kantar.kantar5
                weights['w3'] = kantar.kantar3 - kantar.kantar4
                weights['w2'] = kantar.kantar2 - kantar.kantar3
                weights['w1'] = kantar.kantar1 - kantar.kantar2
            elif getKantarAmount() == 3:
                weights['w3'] = kantar.kantar3 - kantar.kantar4
                weights['w2'] = kantar.kantar2 - kantar.kantar3
                weights['w1'] = kantar.kantar1 - kantar.kantar2
            elif getKantarAmount() == 2:
                weights['w2'] = kantar.kantar2 - kantar.kantar3
                weights['w1'] = kantar.kantar1 - kantar.kantar2
            elif getKantarAmount() == 1:
                weights['w1'] = kantar.kantar1 - kantar.kantar2

            return weights

        def setFormAmount(malAdedi):

            if getKantarAmount() == 5:
                forms = {
                    'form1': djangoForms.MalAlimForm(initial={'kantar': kantar, 'miktar': getMaterialWeights()['w1']}),
                    'form2': djangoForms.MalAlimForm(initial={'kantar': kantar, 'miktar': getMaterialWeights()['w2']}),
                    'form3': djangoForms.MalAlimForm(initial={'kantar': kantar, 'miktar': getMaterialWeights()['w3']}),
                    'form4': djangoForms.MalAlimForm(initial={'kantar': kantar, 'miktar': getMaterialWeights()['w4']}),
                    'form5': djangoForms.MalAlimForm(initial={'kantar': kantar, 'miktar': getMaterialWeights()['w5']}),

                }
                return forms

            if getKantarAmount() == 4:
                forms = {
                    'form1': djangoForms.MalAlimForm(initial={'kantar': kantar, 'miktar': getMaterialWeights()['w1']}),
                    'form2': djangoForms.MalAlimForm(initial={'kantar': kantar, 'miktar': getMaterialWeights()['w2']}),
                    'form3': djangoForms.MalAlimForm(initial={'kantar': kantar, 'miktar': getMaterialWeights()['w3']}),
                    'form4': djangoForms.MalAlimForm(initial={'kantar': kantar, 'miktar': getMaterialWeights()['w4']}),

                }
                return forms

            if getKantarAmount() == 3:
                forms = {
                    'form1': djangoForms.MalAlimForm(initial={'kantar': kantar, 'miktar': getMaterialWeights()['w1']}),
                    'form2': djangoForms.MalAlimForm(initial={'kantar': kantar, 'miktar': getMaterialWeights()['w2']}),
                    'form3': djangoForms.MalAlimForm(initial={'kantar': kantar, 'miktar': getMaterialWeights()['w3']}),

                }
                return forms

            if getKantarAmount() == 2:
                forms = {
                    'form1': djangoForms.MalAlimForm(initial={'kantar': kantar, 'miktar': getMaterialWeights()['w1']}),
                    'form2': djangoForms.MalAlimForm(initial={'kantar': kantar, 'miktar': getMaterialWeights()['w2']}),

                }
                return forms

            if getKantarAmount() == 1:
                forms = {
                    'form1': djangoForms.MalAlimForm(initial={'kantar': kantar, 'miktar': getMaterialWeights()['w1']}),

                }
                return forms

        # print(setFormAmount(getKantarAmount()))

        context = {}
        context['query'] = getLastMalAlimRecords(10)
        context['kantar'] = kantar
        context['forms'] = setFormAmount(getKantarAmount())
        return render(request, context=context, template_name="mainPage/malGiris.html")


def getQueryBuy(queryDict):
    # {'csrfmiddlewaretoken': ['gQJKvsznZiBU8q3ju3TeuQaRf7QpqPW1idLYswdKXtAgyHWsq6iwjkEaIBI0mSTp'], 'kantarNo': [''],
    #  'tarih': [''], 'tedarikci': ['1'], 'malTipi': ['']}
    query = models.MalAlim.objects.all()
    try:
        if queryDict['tarih'][0][0] == ">":
            query = query.filter(kantar__tarih__gte=datetime.strptime(queryDict['tarih'][0][1:], '%d.%m.%Y'))

        elif queryDict['tarih'][0][0] == "<":
            query = query.filter(kantar__tarih__lt=datetime.strptime(queryDict['tarih'][0][1:], '%d.%m.%Y'))

        else:
            print("Hatalı giriş")
    except:
        print("Hatalı tarih modu")

    try:
        query = query.filter(mal=models.Hammadde.objects.get(id=queryDict['malTipi'][0]))
    except:
        pass

    try:
        query = query.filter(kantar__tedarikci=models.Tedarikci.objects.get(id=queryDict['tedarikci'][0]))
    except:
        pass

    try:
        query = query.filter(kantar=models.Kantar.objects.get(id=queryDict['kantarNo'][0]))
    except:
        pass

    print(query)
    return query


def queryTable(request):
    form = djangoForms.AlimKayitlarQueryForm()
    context = {}
    context['form'] = form
    if request.method == "POST":
        # print(dict(request.POST))
        context['query'] = getQueryBuy(dict(request.POST))
        form = djangoForms.AlimKayitlarQueryForm(request.POST)

    return render(request, 'mainPage/buyQueryTable.html', context=context)


def sell(request):
    pass
