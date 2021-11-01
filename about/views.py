from django.shortcuts import render
from site_settings.models import *
from .models import *
import os
from contacts.models import *


def about(request, lang='ru'):
    data = {
        'page': 'about',
        'banners': Banner.objects.all(),
        'workers': Team.objects.all(),
        'meta': MetaTags.objects.all(),
        'favicons': Favicon.objects.all(),
        'head_tags': HeadTags.objects.all(),
        'lang': lang,
        'contact_info': {
            'phones': Phone.objects.all(),
            'emails': EMail.objects.all(),
            'addresses': Address.objects.all(),
            'social': SocialLink.objects.all()
        },
    }
    contact_info = {
        'name': request.GET.get('name'),
        'phone': request.GET.get('phone'),
        'email': request.GET.get('email'),
        'message': request.GET.get('message'),
    }
    if contact_info['name'] or contact_info['phone'] or contact_info['message']:
        os.system(
            f'bot_engine/main.py --name "{contact_info["name"]}" --phone "{contact_info["phone"]}" '
            f'--email "{contact_info["email"]}" --message "{contact_info["message"]}"')
        data['success_sent'] = True

    return render(request, 'about/index.html', context=data)
