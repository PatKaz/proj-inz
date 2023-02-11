from django import forms
from .models import Pred_car, Model 

class Pred_car_Form(forms.ModelForm):
    class Meta:
        model=Pred_car
        fields= '__all__'
        widgets = {
            'mark': forms.Select(attrs={ 'class': 'form-select' }),
            'model': forms.Select(attrs={ 'class': 'form-select' }),

            'year': forms.Select(attrs={ 'class': 'form-control' }),
            'mileage': forms.TextInput(attrs={ 'class': 'form-control' }),
            'vol_engine': forms.TextInput(attrs={ 'class': 'form-control','placeholder': 'Jeśli wybrałeś silnik elektryczny wpisz 1' }),

            'fuel': forms.Select(attrs={ 'class': 'form-select' }),
            'province': forms.Select(attrs={ 'class': 'form-select' }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['model'].queryset=Model.objects.none()

        if 'mark' in self.data:
            try:
                mark_id=int(self.data.get('mark'))
                self.fields['model'].queryset=Model.objects.filter(mark_id=mark_id).order_by('name')
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['model'].queryset= self.instance.mark.model_set.order_by('name')

