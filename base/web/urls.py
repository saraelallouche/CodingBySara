from django.urls import path

from .views import HomeView, send_mail_page

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('contact/', send_mail_page, name='send_mail_page'),

]
