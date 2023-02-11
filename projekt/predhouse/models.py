from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


CHOICES_ROOM_NUM = [
    (1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),(6, '6'),(7, '7')]


CHOICES_DISTRICT= [
    (1, 'Bemowo'),(2, 'Białołęka'),(3, 'Bielany'),(4, 'Centrum'),(5, 'Mokotów'),(6, 'Ochota'),(7, 'Praga-Południe'),
    (8, 'Praga-Północ'),(9, 'Targówek'),(10, 'Ursus'),(11, 'Ursynów'),(12, 'Wawer'),(13, 'Wilanów'),(14, 'Wola'),
    (15, 'Włochy'),(16, 'Śródmieście'),(17, 'Żoliborz')
    ]
CHOICES_FLOOR=[
(1, 'Pierwsze'),(2, 'Drugie'),(3, 'Trzecie'),(4, 'Czwarte'),(5, 'Piąte'),(6, 'Szóste'),(7, 'Siudme'),
    (8, 'Ósme'),(9, 'Dziewiąte'),(10, 'Dziesiąte'),(11, 'Jedenaste')

]

CHOICES_NUM= [(0, 'Nie'),(1, 'Tak')]


class Pred_house(models.Model):
    area=models.PositiveBigIntegerField( verbose_name="Mertaż",  validators=[ MaxValueValidator(300), MinValueValidator(10)],blank=False)
    room_num=models.PositiveIntegerField(choices=CHOICES_ROOM_NUM,blank=False, verbose_name="Liczba pokoi")
    floor=models.PositiveIntegerField(choices=CHOICES_FLOOR,blank=False, verbose_name="Piętro")
    total_floor=models.PositiveIntegerField(verbose_name="Ilość pięter",  validators=[ MaxValueValidator(50), MinValueValidator(1)],blank=False)
    year_built=models.PositiveIntegerField(verbose_name="Rok budynku",  validators=[ MaxValueValidator(2023), MinValueValidator(1900)],blank=False)
    dish_washer=models.PositiveIntegerField(choices=CHOICES_NUM,blank=False, verbose_name="Zmywarka")
    tv_set=models.PositiveIntegerField(choices=CHOICES_NUM,blank=False, verbose_name="Telewizor")
    washer=models.PositiveIntegerField(choices=CHOICES_NUM,blank=False, verbose_name="Pralka")
    balcony=models.PositiveIntegerField(choices=CHOICES_NUM,blank=False, verbose_name="Balkon")
    basement=models.PositiveIntegerField(choices=CHOICES_NUM,blank=False, verbose_name="Piwnica")
    elevator=models.PositiveIntegerField(choices=CHOICES_NUM,blank=False, verbose_name="Winda")
    internet=models.PositiveIntegerField(choices=CHOICES_NUM,blank=False, verbose_name="Internet")
    available_for_students=models.PositiveIntegerField(choices=CHOICES_NUM,blank=False, verbose_name="Dla studentów")
    two_level=models.PositiveIntegerField(choices=CHOICES_NUM,blank=False, verbose_name="Dwupoziomowe")
    garden=models.PositiveIntegerField(choices=CHOICES_NUM,blank=False, verbose_name="Ogród")
    district=models.PositiveIntegerField(choices=CHOICES_DISTRICT,blank=False, verbose_name="Dzielnica")

    class Meta:
        verbose_name = "Predykcja wynajmu mieszkania w warszawie"
        verbose_name_plural = "Predykcja wynajmu mieszkania w warszawie"