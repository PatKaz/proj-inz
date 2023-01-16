from django import forms
from .models import Pred_house 

class Pred_house_Form(forms.ModelForm):
    class Meta:
        model=Pred_house
        fields= '__all__'
        widgets = {
            'area': forms.TextInput(attrs={ 'class': 'form-control'  }),
            'room_num': forms.Select(attrs={ 'class': 'form-select'}),
            'floor': forms.Select(attrs={ 'class': 'form-select' }),
            'total_floor': forms.TextInput(attrs={ 'class': 'form-control' }),
            'year_built': forms.TextInput(attrs={ 'class': 'form-control' }),
            'dish_washer':forms.Select(attrs={ 'class': 'form-select' }),
            'tv_set': forms.Select(attrs={ 'class': 'form-select' }),
            'washer': forms.Select(attrs={ 'class': 'form-select' }),


            'balcony': forms.Select(attrs={ 'class': 'form-select' }),
            'basement': forms.Select(attrs={ 'class': 'form-select' }),
            'elevator': forms.Select(attrs={ 'class': 'form-select' }),
            'internet': forms.Select(attrs={ 'class': 'form-select' }),
            'available_for_students': forms.Select(attrs={ 'class': 'form-select' }),
            'two_level': forms.Select(attrs={ 'class': 'form-select' }),
            'garden': forms.Select(attrs={ 'class': 'form-select' }),
            'district': forms.Select(attrs={ 'class': 'form-select'}),
        }

