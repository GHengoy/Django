from django.urls import path

from . import views

app_name = 'dashboard'  #앱 이름 설정 
urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('404.html', views.error, name='error'),
    path('blank.html', views.blank, name='blank'),
    path('buttons.html', views.buttons, name='buttons'),
    path('cards.html', views.cards, name='cards'),
    path('charts.html', views.charts, name='charts'),
    path('forgot-passwrod.html', views.forgot_passwrod, name='forgot_passwrod'),
    path('login.html', views.login, name='login'),
    path('register.html', views.register, name='register'),
    path('tables.html', views.tables, name='tables'),
    path('utilities-animation.html', views.utilities_animation, name='utilities_animation'),
    path('utilities-border.html', views.utilities_border, name='utilities_border'),
    path('utilities-color.html', views.utilities_color, name='utilities_color'),
    path('utilities-other.html', views.utilities_other, name='utilities_other'),
]