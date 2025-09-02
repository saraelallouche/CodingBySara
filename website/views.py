from typing import Any
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from website.form.contactForm import ContactForm  # new

# Create your views here.
class HomeView(TemplateView):  # new
    template_name = "home/base.html"
    form=ContactForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        context['page']='home'
        return context


class AboutView(TemplateView):  # new
    template_name = "about_me/base.html"


class SkillsView(TemplateView):  # new
    template_name = "skills/base.html"


class ContactView(TemplateView):  # new
    template_name = "contact/base.html"
    form=ContactForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        context['page']='contact'
        return context


class PortfolioView(TemplateView):  # new
    template_name = "portfolio/base.html"


def send_mail_page(request):
    next_page = request.POST.get('next', '/')  # par défaut home si absent
    print(next_page)
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            cleaned = form.cleaned_data
            subject = "SaraWeb : Nouveau message"
            message = f"""
            Nouveau message reçu :

            Nom : {cleaned['last_name']}
            Prénom : {cleaned['first_name']}
            Email : {cleaned['email']}

            Message :
            {cleaned['message']}
            """
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, ['saraelallouche@hotmail.fr'])
                messages.success(request, "Votre message a bien été envoyé.")
            except Exception as e:
                messages.error(request, f"Une erreur est survenue lors de l'envoie de l'email. ")
    else:
        form = ContactForm()

    if 'contact' in next_page:
        return render(request, 'contact/base.html', {'form': form, 'page':'contact'})
    else:
        return render(request, 'home/base.html', {'form': form, 'scroll_to_contact': True, 'page':'home'})

