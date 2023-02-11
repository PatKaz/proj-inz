
from django.test import TestCase
import requests
import json
from .models import Pred_house, CHOICES_ROOM_NUM, CHOICES_FLOOR, CHOICES_NUM, CHOICES_DISTRICT
import xgboost as xgb
import pandas as pd

class Pred_houseTestCase(TestCase):
    def setUp(self):
        self.pred_house = Pred_house.objects.create(
            area=50,
            room_num=2,
            floor=2,
            total_floor=5,
            year_built=2000,
            dish_washer=1,
            tv_set=1,
            washer=1,
            balcony=1,
            basement=1,
            elevator=1,
            internet=1,
            available_for_students=1,
            two_level=1,
            garden=1,
            district=1
        )
        
    
    def test_pred_house_area(self):
        self.assertEqual(self.pred_house.area, 50)
    
    def test_pred_house_room_num(self):
        self.assertEqual(self.pred_house.room_num, 2)
        
    def test_pred_house_floor(self):
        self.assertEqual(self.pred_house.floor, 2)
        
    def test_pred_house_total_floor(self):
        self.assertEqual(self.pred_house.total_floor, 5)
        
    def test_pred_house_year_built(self):
        self.assertEqual(self.pred_house.year_built, 2000)
        
    def test_pred_house_dish_washer(self):
        self.assertEqual(self.pred_house.dish_washer, 1)
        
    def test_pred_house_tv_set(self):
        self.assertEqual(self.pred_house.tv_set, 1)
        
    def test_pred_house_washer(self):
        self.assertEqual(self.pred_house.washer, 1)
        
    def test_pred_house_balcony(self):
        self.assertEqual(self.pred_house.balcony, 1)
        
    def test_pred_house_basement(self):
        self.assertEqual(self.pred_house.basement, 1)
        
    def test_pred_house_elevator(self):
        self.assertEqual(self.pred_house.elevator, 1)
        
    def test_pred_house_internet(self):
        self.assertEqual(self.pred_house.internet, 1)
    
        
class PredHouseAPITest(TestCase):
    def test_get_latest_pred_house(self):
        response = requests.get('http://127.0.0.1:8000/api/pred_house/latest/')
        self.assertEqual(response.status_code, 200)
        pred_house = json.loads(response.text)
        print("Test pobrania danych z API - OK  :",pred_house)



class PredictPriceHouse(TestCase):
    def test_predict_price_house(self):
        response = requests.get('http://127.0.0.1:8000/api/pred_house/latest/')
        self.assertEqual(response.status_code, 200)
        pred_house = response.json()
        to_predict = {}
        for key, value in pred_house.items():
            to_predict[key] = [value]
        loaded_model = xgb.Booster()
        loaded_model.load_model("C:\\Users\\patry\\OneDrive\\Pulpit\\inzzza\\model_sklearn.json")  
        pred = xgb.DMatrix(pd.DataFrame(to_predict))
        price=loaded_model.predict(pred)
        print("Test pobrania z Api i predykcji - OK, cena wynosi: ",price, " zł")

 

class PredTestHouse(TestCase):
    def test_create_instance_with_user_input(self):
        area = int(input("Podaj metraż: "))
        room_num = int(input("Podaj liczbe pokoi: "))
        floor = int(input("Podaj piętro: "))
        total_floor = int(input("Podaj ilość kondygnacji: "))
        year_built = int(input("Podaj rok budowy: "))
        dish_washer = int(input("Czy jest zmywarka? (1 TAK, 0 NIE) "))
        tv_set = int(input("Czy jest telewizor? (1 TAK, 0 NIE) "))
        washer = int(input("Czy jest pralka? (1 TAK, 0 NIE) "))
        balcony = int(input("Czy jest balkon? (1 TAK, 0 NIE) "))
        basement = int(input("Czy jest piwnica? (1 TAK, 0 NIE) "))
        elevator = int(input("Czy jest winda? (1 TAK, 0 NIE) "))
        internet = int(input("Czy jest internet? (1 TAK, 0 NIE) "))
        available_for_students = int(input("Czy jest dla studentów? (1 TAK, 0 NIE)"))
        two_level = int(input("Czy jest dwupoziomowe? (1 TAK, 0 NIE) "))
        garden = int(input("Czy jest ogród? (1 TAK, 0 NIE) "))
        district = int(input("Podaj nr dzielnicy (1-17): "))
       
        data = {'area': [area], 'room_num': [room_num], 'floor': [floor],
         'total_floor': [total_floor], 'year_built': [year_built], 'dish_washer': [dish_washer],
          'tv_set': [tv_set], 'washer': [washer], 'balcony': [balcony], 'basement': [basement], 'elevator': [elevator], 'internet': [internet], 
          'available_for_students': [available_for_students], 'two_level': [two_level],
        'garden': [garden], 'district': [district]}
       
        loaded_model = xgb.Booster()
        loaded_model.load_model("C:\\Users\\patry\\OneDrive\\Pulpit\\inzzza\\model_sklearn.json")  
        pred = xgb.DMatrix(pd.DataFrame(data))
        price=loaded_model.predict(pred)
        print("Test predykcji ok, cena wynosi: ",price, " zł")


    