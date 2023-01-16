from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('', include('predhouse.urls')),
    path('', include('predcar.urls')),
    path('captcha/', include('captcha.urls'))
]
