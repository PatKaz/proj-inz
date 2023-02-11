from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import Pred_house
from . serializers import Pred_houseSerializers
import pickle
import joblib
import requests
import json
import numpy as np
import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from .forms import Pred_house_Form
from rest_framework import views
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
import xgboost as xgb


class Pred_houseViews(viewsets.ModelViewSet):
  queryset=Pred_house.objects.all()
  serializer_class=Pred_houseSerializers
  def get_object(self):
        return Pred_house.objects.latest('id')
  def latest(self, request):
        latest_model = self.get_queryset().latest('id')
        serializer = self.get_serializer(latest_model)
        return Response(serializer.data)


@login_required
def create_view(request):
    user = request.user
    form = Pred_house_Form()
    if request.method == 'POST':
        form = Pred_house_Form(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('predhouse:predictor_house')
    return render(request, 'pred_house.html', {'form': form})

@api_view(['GET'])
def index(request):
    return_data = {
        "error_code" : "0",
        "info" : "success",
    }
    return Response(return_data)


@login_required
def predictor_house(request):
    user = request.user
    url = 'http://127.0.0.1:8000/api/pred_house/latest'
    response = requests.get(url)
    if response.status_code == 200:
        jk = response.json()
        to_predict = {}
        for key, value in jk.items():
            to_predict[key] = [value]
        loaded_model = xgb.Booster()
        loaded_model.load_model("C:\\Users\\patry\\OneDrive\\Pulpit\\inzzza\\App\\projekt\\model_pred_house.json")  
        pred = xgb.DMatrix(pd.DataFrame(to_predict)) 
        status=loaded_model.predict(pred)
        status=int(status[0])
        house = Pred_house.objects.filter().last
    else:
        print('Nie udało się pobrać modelu')
    context={'status': status,'house': house}
    return render(request, 'predictor_house.html', context)


