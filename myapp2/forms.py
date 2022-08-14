from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

#from CRUDE.myapp2.views import user_logout
from .models import Appointment

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        

        # This below code is used for front end designed
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'Password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class Appointmentform(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['Patient_Name', 'Patient_Age', 'Date_Of_Appointment', 'Time_Of_Appointment']

class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login']
        labels = {'email':'Email'}
