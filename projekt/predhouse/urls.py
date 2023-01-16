from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('pred_house',views.Pred_houseViews)
app_name='predhouse'
urlpatterns = [
     #path('form/', views.form.urls),
     path('api/', include(router.urls)),
     #path('status/', views.app),
     
     
     path('predhouse/add/', views.create_view, name='add'),
     path('predictor_house', views.predictor_house, name='predictor_house'),
     #path('member/<int:pk>/', views.update_view, name='change'),
 
     ##path('pred/ajax/load-models/', views.load_models, name='ajax_load_models'),##
     #path('mymodel/', views.MyModelView.as_view(), name='mymodel'),
     ##path('',views.index),##
    ## path('predict', views.pred)##
]