from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from . import djangoForms
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import djangoForms, models
from django.views.decorators.cache import never_cache
import time
from django.db.models import Q
from django.http import QueryDict


def mainPageView(request):
    if request.user.is_authenticated:
        print(request.user.username)
        return render(request, "mainPage/mainPage.html")

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


@never_cache
def buy(request):
    form1 = djangoForms.BuyForm1()
    form2 = djangoForms.BuyForm2()
    form3 = djangoForms.BuyForm3()
    form4 = djangoForms.BuyForm4()
    form5 = djangoForms.BuyForm5()

    form1a = djangoForms.BuyForm1a()
    form1b = djangoForms.BuyForm1b()
    form1c = djangoForms.BuyForm1c()
    form2a = djangoForms.BuyForm2a()
    form2b = djangoForms.BuyForm2b()
    form2c = djangoForms.BuyForm2c()
    form3a = djangoForms.BuyForm3a()
    form3b = djangoForms.BuyForm3b()
    form3c = djangoForms.BuyForm3c()
    form4a = djangoForms.BuyForm4a()
    form4b = djangoForms.BuyForm4b()
    form4c = djangoForms.BuyForm4c()
    form5a = djangoForms.BuyForm5a()
    form5b = djangoForms.BuyForm5b()
    form5c = djangoForms.BuyForm5c()

    latestRecordId = models.Alimlar.objects.all().latest("alimKodu").alimKodu
    print(latestRecordId)
    latestPlusOne = latestRecordId + 1
    request.session['latestPlusOne'] = latestPlusOne
    context = {'latestPlusOne': latestPlusOne}

    if request.method == "POST":
        form1 = djangoForms.BuyForm1(request.POST)
        form2 = djangoForms.BuyForm2(request.POST)
        form3 = djangoForms.BuyForm3(request.POST)
        form4 = djangoForms.BuyForm4(request.POST)
        form5 = djangoForms.BuyForm5(request.POST)

        form1a = djangoForms.BuyForm1a(request.POST)
        form1b = djangoForms.BuyForm1b(request.POST)
        form1c = djangoForms.BuyForm1c(request.POST)
        form2a = djangoForms.BuyForm2a(request.POST)
        form2b = djangoForms.BuyForm2b(request.POST)
        form2c = djangoForms.BuyForm2c(request.POST)
        form3a = djangoForms.BuyForm3a(request.POST)
        form3b = djangoForms.BuyForm3b(request.POST)
        form3c = djangoForms.BuyForm3c(request.POST)
        form4a = djangoForms.BuyForm4a(request.POST)
        form4b = djangoForms.BuyForm4b(request.POST)
        form4c = djangoForms.BuyForm4c(request.POST)
        form5a = djangoForms.BuyForm5a(request.POST)
        form5b = djangoForms.BuyForm5b(request.POST)
        form5c = djangoForms.BuyForm5c(request.POST)

        if form1.is_valid():
            form1.save()

            return redirect("buy")

    context['form1'] = form1
    context['form2'] = form2
    context['form3'] = form3
    context['form4'] = form4
    context['form5'] = form5

    context['form1a'] = form1a
    context['form1b'] = form1b
    context['form1c'] = form1c
    context['form2a'] = form2a
    context['form2b'] = form2b
    context['form2c'] = form2c
    context['form3a'] = form3a
    context['form3b'] = form3b
    context['form3c'] = form3c
    context['form4a'] = form4b
    context['form4b'] = form4b
    context['form4c'] = form4c
    context['form5a'] = form5a
    context['form5b'] = form5b
    context['form5c'] = form5c

    return render(request, "mainPage/weighing.html", context=context)


def buy1(request):
    latestRecordId = models.MalGiris.objects.all().latest("alimKodu").alimKodu
    # print(latestRecordId)
    latestPlusOne = latestRecordId + 1
    request.session['latestPlusOne'] = latestPlusOne
    context = {'latestPlusOne': latestPlusOne}

    form = djangoForms.MalGirisForm()

    def getPrices(cleanedPostDict):
        queryBySupplier = models.MalGiris.objects.filter(tedarikEden=int(cleanedPostDict['tedarikEden'][0])).order_by(
            "-tarih")[:10]
        materials = []
        for material in cleanedPostDict:
            if 'mal' in material:
                materials.append(material)
                # print(cleanedPostDict[material])
        # print(materials)
        materialQueries = []
        for mat in materials:
            materialQueries.append(models.MalGiris.objects.filter(
                Q(mal1=int(cleanedPostDict[mat][0])) | Q(mal1a=int(cleanedPostDict[mat][0])) | Q(
                    mal1b=int(cleanedPostDict[mat][0])) | Q(mal1c=int(cleanedPostDict[mat][0])) | Q(
                    mal2=int(cleanedPostDict[mat][0])) | Q(mal2a=int(cleanedPostDict[mat][0])) | Q(
                    mal2b=int(cleanedPostDict[mat][0])) | Q(mal2c=int(cleanedPostDict[mat][0])) | Q(
                    mal3=int(cleanedPostDict[mat][0])) | Q(mal3a=int(cleanedPostDict[mat][0])) | Q(
                    mal3b=int(cleanedPostDict[mat][0])) | Q(mal3c=int(cleanedPostDict[mat][0])) | Q(
                    mal4=int(cleanedPostDict[mat][0])) | Q(mal4a=int(cleanedPostDict[mat][0])) | Q(
                    mal4b=int(cleanedPostDict[mat][0])) | Q(mal4c=int(cleanedPostDict[mat][0])) | Q(
                    mal5=int(cleanedPostDict[mat][0])) | Q(mal5a=int(cleanedPostDict[mat][0])) | Q(
                    mal5b=int(cleanedPostDict[mat][0])) | Q(mal5c=int(cleanedPostDict[mat][0]))).order_by("-tarih")[
                                   :5])
        for i in queryBySupplier:
            print(i)

        return queryBySupplier, materialQueries

    if request.method == "POST":
        form = djangoForms.MalGirisForm(request.POST)
        submit_button = request.POST.get('submit_button')
        supplier = models.Tedarikci.objects.get(id=form.data['tedarikEden'])
        mal=models.Hammadde.objects.get(id=int(request.POST.get("mal1")))
        context['supplier'] = supplier
        context['mal'] = mal

        if submit_button == "Fiyat":
            post = dict(request.POST)
            post2 = {}
            for item in post:
                if "" in post[item] or item == "csrfmiddlewaretoken" or item == "initial-tarih":
                    pass
                else:
                    post2[item] = post[item]
            queryBySupplier, materialQueries = getPrices(post2)

            context["queryBySupplier"] = queryBySupplier
            context['materialQueries'] = materialQueries

            data_copy = QueryDict(mutable=True)
            data_copy.update(request.POST)

            # Clear the value of the field
            data_copy.pop('birimFiyat1', None)

            # Update the form's data with the modified copy
            form.data = data_copy

            context['form'] = form

            print("Fiyata basıldı")
            return render(request, "mainPage/weighing2.html", context=context)


        else:
            if form.is_valid():
                form.save()

                # print(type(post[item]))

                # print(post2)

                #         print(item)
                # print(request.POST)
                # # print("-----------------------")
                # print(type(request.POST)==type({}))

                return redirect("buy")

    context['form'] = form

    return render(request, "mainPage/weighing2.html", context=context)
