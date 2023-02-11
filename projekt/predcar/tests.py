from django.test import TestCase
from .models import Pred_car,Mark, Model
import requests
import json
import xgboost as xgb
import pandas as pd

class MarkTestCase(TestCase):
    def setUp(self):
        self.mark=Mark(name="TestMark")
        self.mark.save()
        self.assertIsNotNone(self.mark.id, 'Test tworzenia mark prawidłowy')
        print('Model mark - test ok')
        
class ModelTestCase(TestCase):
    def setUp(self):
        mark = Mark.objects.create(name='Volkswagen')
        Model.objects.create(mark=mark, name='golf')
        Model.objects.create(mark=mark, name='jetta')

    def test_model_name(self):
        model1 = Model.objects.get(id=1)
        model2 = Model.objects.get(id=2)
        self.assertEqual(model1.name, 'golf')
        self.assertEqual(model2.name, 'jetta')
        print('Model model - test ok', model2.name)
    def test_model_mark(self):
        model1 = Model.objects.get(id=1)
        model2 = Model.objects.get(id=2)
        self.assertEqual(model1.mark.name, 'Volkswagen')
        self.assertEqual(model2.mark.name, 'Volkswagen')
        print('Model mark - test ok', model2.mark.name)
        


class Pred_carTestCase(TestCase):
    def setUp(self):
        self.mark = Mark.objects.create(name="TestMark")
        self.model = Model.objects.create(name="TestModel", mark=self.mark)
        self.pred_car = Pred_car.objects.create(mark=self.mark, model=self.model, year=2001, mileage=300000, vol_engine=2000, fuel=0, province=5)

    def test_pred_car_creation(self):
        self.pred_car.save()
        print("Dane testowe poprawnie zapisane w modelu testowym")
        self.assertIsNotNone(self.pred_car.id)
        self.assertEqual(self.pred_car.mark.name, "TestMark")
        self.assertEqual(self.pred_car.model.name, "TestModel")
        self.assertEqual(self.pred_car.year, 2001)
        self.assertEqual(self.pred_car.mileage, 300000)
        self.assertEqual(self.pred_car.vol_engine, 2000)
        self.assertEqual(self.pred_car.fuel, 0)
        self.assertEqual(self.pred_car.province, 5)
    
    def test_pred_car_fuel_choices(self):
        self.assertEqual(self.pred_car.get_fuel_display(), "Diesel")
        test=self.pred_car.get_fuel_display()
        print("test fuel - OK : ",test)
    def test_pred_car_province_choices(self):
        self.assertEqual(self.pred_car.get_province_display(), "Małopolskie")
        test=self.pred_car.get_province_display()
        print("test province - OK : ",test)
    def test_pred_car_year_choices(self):
        self.assertEqual(self.pred_car.get_year_display(), "2001")
        test=self.pred_car.get_year_display()
        print("test year - OK : ",test)


class PredcarAPITest(TestCase):
    def test_get_latest_pred_car(self):
        response = requests.get('http://127.0.0.1:8000/api/pred_car/latest')
        self.assertEqual(response.status_code, 200)
        pred_car = json.loads(response.text)
       
        print("Test pobrania danych z API - OK  :",pred_car)

class PredictPricecar(TestCase):
    def test_predict_price_car(self):
        response = requests.get('http://127.0.0.1:8000/api/pred_car/latest')
        self.assertEqual(response.status_code, 200)
        pred_car = response.json()
        to_predict = {}
        for key, value in pred_car.items():
            to_predict[key] = [value]
        loaded_model = xgb.Booster()
        loaded_model.load_model("C:\\Users\\patry\\OneDrive\\Pulpit\\inzzza\\model_car.json")  
        pred = xgb.DMatrix(pd.DataFrame(to_predict))
        price=loaded_model.predict(pred)
        print("Test pobrania z Api i predykcji - OK,       cena wynosi: ",price, " zł")


class PredTestCar(TestCase):
    def test_create_instance_with_user_input_car(self):
        mark=int(input("Podaj marke 1-23: "))
        model=int(input("Podaj model 1-283: "))
        year=int(input("Podaj rok produkcji: "))
        mileage=int(input("Podaj przebieg: "))
        vol_engine=int(input("Podaj pojemność: "))
        fuel=int(input("Podaj typ sylnika 0-4: "))
        province=int(input("Podaj województwo 0-15: "))


        data = {'mark': [mark], 'model': [model], 'year': [year],
         'mileage': [mileage], 'vol_engine': [vol_engine], 'fuel': [fuel],
          'province': [province]}

        loaded_model = xgb.Booster()
        loaded_model.load_model("C:\\Users\\patry\\OneDrive\\Pulpit\\inzzza\\model_car.json")  
        pred = xgb.DMatrix(pd.DataFrame(data))
        price=loaded_model.predict(pred)
        print("Test predykcji ok, cena wynosi: ",price, " zł")