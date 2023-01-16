from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('pred_car',views.Pred_carViews)
app_name='predcar'
urlpatterns = [
     
     path('api/', include(router.urls)),
   
    
     
     path('predcar/add/', views.create_view, name='add'),
     path('predictor_car', views.predictor_car, name='predictor_car'),
     
 
     path('pred/ajax/load-models/', views.load_models, name='ajax_load_models'),
    
]