from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('pred_house',views.Pred_houseViews)
app_name='predhouse'
urlpatterns = [

     path('api/', include(router.urls)),
     
     path('predhouse/add/', views.create_view, name='add'),
     path('predictor_house', views.predictor_house, name='predictor_house'),
    
]