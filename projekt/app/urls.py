
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('start', views.start, name="start"),
    path('home', views.home, name="home"),
    path('login/', views.login_user, name="login"), 
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.create_user, name="register"),
    path('profil/', views.profil, name="profil"),
    path('edit/', views.edit, name="edit"),
    path('change_password/', views.change_password, name="change_password"),
    path('social-auth/', include('social_django.urls', namespace='social')),

      path('password_reset/',auth_views.PasswordResetView.as_view(template_name="account/password_reset.html"),name='password_reset'),
      path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"),name='password_reset_done'),
      path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html"),name='password_reset_confirm'),
      path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html" ),name='password_reset_complete'),

      path('reg/', views.reg, name="reg"),
      path('pp/', views.pp, name="pp"),
      path('email/', views.contact, name="email"),
      path('contact/', views.contact, name="contact"),
]
