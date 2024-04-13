from django.shortcuts import render, redirect
from yoolink.ycms.models import FAQ, UserSettings, Message, Product, OpeningHours, TextContent, fileentry, Galerie, GaleryImage
import datetime
from django.http import HttpResponseRedirect

def get_opening_hours():
    opening_hours = {}
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    for day in days:
        if OpeningHours.objects.filter(day=day).exists():
            opening_hours[f"opening_{day.lower()}"] = OpeningHours.objects.get(day=day)
        else:
            opening_hours[f"opening_{day.lower()}"] = None
            
    user_settings = UserSettings.objects.filter(user__is_staff=False)
    if user_settings.exists():
        user_settings = user_settings.first()
        opening_hours["owner_data"] = user_settings
    return opening_hours


def load_index(request):
    faq = FAQ.objects.all()

    context = {
        'FAQ': faq,
    }

    # Text Contents
    if TextContent.objects.filter(name="main_hero").exists():
        context["heroText"] = TextContent.objects.get(name='main_hero')



    if TextContent.objects.filter(name="main_cms").exists():
        context["cmsText"] = TextContent.objects.get(name='main_cms')

    if TextContent.objects.filter(name="main_team").exists():
        context["teamText"] = TextContent.objects.get(name='main_team')


    # Autoglas Leistungen

    if TextContent.objects.filter(name="main_agleistungen").exists():
        context["agdienstText"] = TextContent.objects.get(name='main_agleistungen')

    if TextContent.objects.filter(name="main_agdienst_1").exists():
        context["agdienst1Text"] = TextContent.objects.get(name='main_agdienst_1')
        
    if TextContent.objects.filter(name="main_agdienst_2").exists():
        context["agdienst2Text"] = TextContent.objects.get(name='main_agdienst_2')
        
    if TextContent.objects.filter(name="main_agdienst_3").exists():
        context["agdienst3Text"] = TextContent.objects.get(name='main_agdienst_3')

    if TextContent.objects.filter(name="main_agdienst_4").exists():
        context["agdienst4Text"] = TextContent.objects.get(name='main_agdienst_4')


    # HDDienstleistungen        
    if TextContent.objects.filter(name="main_hdleistungen").exists():
        context["dienstText"] = TextContent.objects.get(name='main_hdleistungen')

    if TextContent.objects.filter(name="main_dienst_1").exists():
        context["dienst1Text"] = TextContent.objects.get(name='main_dienst_1')
        
    if TextContent.objects.filter(name="main_dienst_2").exists():
        context["dienst2Text"] = TextContent.objects.get(name='main_dienst_2')
        
    if TextContent.objects.filter(name="main_dienst_3").exists():
        context["dienst3Text"] = TextContent.objects.get(name='main_dienst_3')


    # Galerie
    if TextContent.objects.filter(name="main_galerie").exists():
        context["galerieText"] = TextContent.objects.get(name='main_galerie')
 
    if Galerie.objects.filter(place='main_Galery').exists():
        context["mainGalery"] = Galerie.objects.get(place='main_Galery').images.all()

    if TextContent.objects.filter(name="main_Galery_1").exists():
        context["galerie1Text"] = TextContent.objects.get(name='main_Galery_1')
        
    if TextContent.objects.filter(name="main_Galery_2").exists():
        context["galerie2Text"] = TextContent.objects.get(name='main_Galery_2')

    # Images
    if fileentry.objects.filter(place='main_hero_1').exists():
        context["heroImage1"] = fileentry.objects.get(place='main_hero_1')
    if fileentry.objects.filter(place='main_hero_2').exists():
        context["heroImage2"] = fileentry.objects.get(place='main_hero_2')
    if fileentry.objects.filter(place='main_hero_3').exists():
        context["heroImage3"] = fileentry.objects.get(place='main_hero_3')

    if fileentry.objects.filter(place='main_team').exists():
        context["teamImage"] = fileentry.objects.get(place='main_team')


    context["user_settings"] = UserSettings.objects.filter(user__is_staff=False).first() 
    context.update(get_opening_hours())
    return render(request, 'pages/index.html', context=context)

def kontaktform(request):
    success = False
    current_date_time = datetime.datetime.now()
    if request.method == 'POST':
        Message.objects.create(name = request.POST["name"], email=request.POST['email'], message=request.POST['message'], date=current_date_time, seen=False)

        return render(request, 'pages/kontakt.html', {'success': True})

    return render(request, 'pages/kontakt.html', {'success': success})


def impressum(request):
    context = {}
    context.update(get_opening_hours())
    return render(request, 'pages/impressum.html', context)

def datenschutz(request):
    context = {}
    context.update(get_opening_hours())
    return render(request, 'pages/datenschutz.html', context)

def cookies(request):
    context = {}
    context.update(get_opening_hours())
    return render(request, 'pages/cookies.html', context)