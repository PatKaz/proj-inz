from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Mark(models.Model):
    name = models.TextField(max_length=10,blank=False,verbose_name="Marka")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Marka"
        verbose_name_plural = "Marki"
    
 
class Model(models.Model):

    
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, verbose_name="Marka",blank=False,)
    name = models.TextField(max_length=10,verbose_name="Model",blank=False,)
 
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Model"
        verbose_name_plural = "Modele"


class Pred_car(models.Model):
    CHOICES_FUEL = [
    (0, 'Diesel'),(1, 'Elektryczny'),(2, 'Benzyna'),(3, 'Hybryda'),(4, 'LPG'),]
    
    CHOICES_PROVINCE = [
    (0, 'Dolnośląskie'),(1, 'Kujawsko-pomorskie'),(2, 'Lubelskie'),(3, 'Lubuskie'),(4, 'Mazowieckie'), (5, 'Małopolskie'),(6, 'Opolskie'),(7, 'Podkarpackie'),(8, 'Podlaskie'),
     (9, 'Pomorskie'),(10, 'Warmińsko-mazurskie'),(11, 'Wielkopolskie'),(12, 'Zachodniopomorskie'), (13, 'Łódzkie'),(14, 'Śląskie'),(15, 'Świętokrzyskie')
    ]
    CHOICES_YEAR = [
    (1992, '1992'),(1993, '1993'),(1994, '1994'),(1995, '1995'),(1996, '1996'),
    (1997, '1997'),(1998, '1998'),(1999, '1999'),(2000, '2000'),(2001, '2001'),(2002, '2002'),(2003, '2003'),(2004, '2004'),(2005, '2005'),(2006, '2006'),(2007, '2007'),(2008, '2008'),
    (2009, '2009'),(2010, '2010'),(2011, '2011'),(2012, '2012'),(2013, '2013'),(2014, '2014'),(2015, '2015'),(2016, '2016'),(2017, '2017'),(2018, '2018'),(2019, '2019'),(2020, '2020'),
    (2021, '2021'),(2022, '2022')]

    
    mark=models.ForeignKey(Mark, on_delete=models.SET_NULL, blank=False, null=True,verbose_name="Marka")
    model=models.ForeignKey(Model, on_delete=models.SET_NULL,blank=False, null=True,verbose_name="Model")
    
    year=models.PositiveIntegerField(choices=CHOICES_YEAR,verbose_name="Rok produkcji",blank=False)
    mileage=models.PositiveIntegerField( verbose_name="Przebieg km:   max przebieg do 2000000km",validators=[ MaxValueValidator(2000000), MinValueValidator(1)],blank=False)
    vol_engine=models.PositiveIntegerField(max_length=6, verbose_name="Pojemniść silnika : między 500cm3 a 5000cm3",validators=[ MaxValueValidator(5000), MinValueValidator(0)],blank=False)
    
    fuel=models.PositiveIntegerField(max_length=10,choices=CHOICES_FUEL,blank=False, verbose_name="Rodzaj paliwa")
    province=models.PositiveIntegerField(max_length=10,choices=CHOICES_PROVINCE,blank=False, verbose_name="Województwo")

    class Meta:
        verbose_name = "Predykcja"
        verbose_name_plural = "Predykcje"
    

