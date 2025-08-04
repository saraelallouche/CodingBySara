from django.urls import path
from django.conf.urls.i18n import set_language

from .views import AboutView, ContactView, HomeView, PortfolioView, SkillsView, send_mail_page

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about", AboutView.as_view(), name="about"),
    path("skills", SkillsView.as_view(), name="skills"),
    path("contact", ContactView.as_view(), name="contact"),
    path("portfolio", PortfolioView.as_view(), name="portfolio"),
    path('send_mail_page/', send_mail_page, name='send_mail_page'),
    path('i18n/setlang/', set_language, name='set_language'),

]
