from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import Mark,Model,Pred_car
from . serializers import pred_carSerializers
import pickle
import joblib
import requests
import json
import numpy as np
import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from .forms import Pred_car_Form
from rest_framework import views
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
import xgboost as xgb
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


#loaded_model = joblib.load(open('C:\\Users\\patry\\OneDrive\\Pulpit\\inzzza\\carr', 'rb'))

class Pred_carViews(viewsets.ModelViewSet,):   
    queryset=Pred_car.objects.all()
    serializer_class=pred_carSerializers

    def get_object(self):
        return Pred_car.objects.latest('id')
    def latest(self, request):
        latest_model = self.get_queryset().latest('id')
        serializer = self.get_serializer(latest_model)
        return Response(serializer.data)





@login_required
def create_view(request):
    user = request.user
    form = Pred_car_Form()
    if request.method == 'POST':
        form = Pred_car_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('predcar:predictor_car')
    return render(request, 'pred_car.html', {'form': form})

def load_models(request):
    mark_id = request.GET.get('mark_id')
    modelss = Model.objects.filter(mark_id=mark_id).all()
    return render(request, 'drop_list.html', {'modelss': modelss})



@api_view(['GET'])
def index(request):
    return_data = {
        "error_code" : "0",
        "info" : "success",
    }
    return Response(return_data)

@login_required
def predictor_car(request):
    user = request.user
    url = 'http://127.0.0.1:8000/api/pred_car/latest'
    response = requests.get(url)
    if response.status_code == 200:
        jk = response.json()
        k = np.array(list(jk.values()))

        to_predict = {}
        for key, value in jk.items():
            to_predict[key] = [value]
        loaded_model = xgb.Booster()
        #dodać prawidłową scieżke do model_car
        loaded_model.load_model("C:\\Users\\patry\\OneDrive\\Pulpit\\inzzza\\model_car.json")  
        pred = xgb.DMatrix(pd.DataFrame(to_predict)) 
        status=loaded_model.predict(pred)
       
        formatted_data = []

        for i, (key, value) in enumerate(jk.items(), 1):
            formatted_data.append(value)
        v1, v2, v3, v4, v5, v6, v7 = formatted_data
        stat=int(status[0])
        mark=Mark.objects.filter(pk=v1).last
        model=Model.objects.filter(pk=v2).last
        car = Pred_car.objects.filter().last
    else:
        print('Nie udało się pobrać modelu')
    context={'stat': stat,'car': car,'mark':mark,'model':model}
    return render(request, 'predictor_car.html', context)

