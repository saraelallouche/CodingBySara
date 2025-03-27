from django.views.generic import TemplateView  # new

# Create your views here.
class HomeView(TemplateView):  # new
    template_name = "home/base.html"


from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render

def send_mail_page(request):
    context = {}

    if request.method == 'POST':
        address = 'saraelallouche@hotmail.fr'
        subject = 'SaraWeb : Nouveau Message '
        
        # Récupération des informations du formulaire
        first_name = request.POST.get('first-name', '').strip()
        last_name = request.POST.get('last-name', '').strip()
        email = request.POST.get('email', '').strip()
        message_content = request.POST.get('message', '').strip()

        # Vérification que tous les champs sont remplis
        if first_name and last_name and email and message_content:
            message = f"""
            Nouveau message reçu depuis SaraWeb :
            
            Nom : {last_name}
            Prénom : {first_name}
            Email : {email}
            
            Message :
            {message_content}
            """
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    
    return render(request, "home/base.html", context)

