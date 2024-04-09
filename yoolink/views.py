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

    if TextContent.objects.filter(name="main_responsive").exists():
        context["responsiveText"] = TextContent.objects.get(name='main_responsive')

    if TextContent.objects.filter(name="main_cms").exists():
        context["cmsText"] = TextContent.objects.get(name='main_cms')

    if TextContent.objects.filter(name="main_price").exists():
        context["priceText"] = TextContent.objects.get(name='main_price')

    if TextContent.objects.filter(name="main_team").exists():
        context["teamText"] = TextContent.objects.get(name='main_team')


    # HDDienstleistungen        
    if TextContent.objects.filter(name="main_hdleistungen").exists():
        context["dienstText"] = TextContent.objects.get(name='main_hdleistungen')

    if TextContent.objects.filter(name="main_dienst_1").exists():
        context["dienst1Text"] = TextContent.objects.get(name='main_dienst_1')
        
    if TextContent.objects.filter(name="main_dienst_2").exists():
        context["dienst2Text"] = TextContent.objects.get(name='main_dienst_2')
        
    if TextContent.objects.filter(name="main_dienst_3").exists():
        context["dienst3Text"] = TextContent.objects.get(name='main_dienst_3')


    # Galery
    if Galerie.objects.filter(place='main_hero').exists():
        context["heroImages"] = Galerie.objects.get(place='main_hero').images.all()
        
    if Galerie.objects.filter(place='main_responsive_desktop').exists():
        context['responsiveDesktopImages'] = Galerie.objects.get(place='main_responsive_desktop').images.all()
        
    if Galerie.objects.filter(place='main_responsive_handy').exists():
        context['responsiveHandyImages'] = Galerie.objects.get(place='main_responsive_handy').images.all()

    # Images
    if fileentry.objects.filter(place='main_cms').exists():
        context["cmsImage"] = fileentry.objects.get(place='main_cms')

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