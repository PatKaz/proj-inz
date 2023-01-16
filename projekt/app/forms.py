from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User 
from django import forms
from captcha.fields import CaptchaField

class EditForm(UserChangeForm):
    password=forms.CharField(label="", widget= forms.TextInput(attrs={'type': 'hidden'}) )
    email=forms.EmailField( label="",widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email'}) )
    first_name= forms.CharField(label="",max_length=100, widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Imię'}) )
    last_name=forms.CharField(label="", max_length=100,widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nazwisko'}) )
    class Meta:
        model=User 
        fields= ('first_name','last_name', 'email', 'password')





class SignUpForm(UserCreationForm):
    email=forms.EmailField( label="",widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email'}) )
    first_name= forms.CharField(label="",max_length=100, widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Imię'}) )
    last_name=forms.CharField(label="", max_length=100,widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nazwisko'}) )
    captcha=CaptchaField(label="")
    class Meta:
        model= User
        fields= ('username', 'first_name','last_name', 'email', 'password1','password2')
     
    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='from-control'
        self.fields['username'].widget.attrs['placeholder']='  Login'
        self.fields['username'].label=''
        self.fields['username'].help_text=''

        self.fields['password1'].widget.attrs['class']='from-control'
        self.fields['password1'].widget.attrs['placeholder']= '  Hasło'
        self.fields['password1'].label=''
        self.fields['password1'].help_text=''

        
        self.fields['password2'].widget.attrs['class']='from-control'
        self.fields['password2'].widget.attrs['placeholder']='  Powtórz hasło'
        self.fields['password2'].label=''
        self.fields['password2'].help_text=''
      
class EmailForm(forms.Form):
    name=forms.CharField(label="", max_length=20,widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Imię'}))
    #email=forms.EmailField(label="", widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email'}) )
    telephone=forms.CharField(label="", widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nr telefonu'}))
    content=forms.CharField(label="", widget= forms.Textarea(attrs={'class': 'form-control','placeholder': 'Treść wiadomości'}))