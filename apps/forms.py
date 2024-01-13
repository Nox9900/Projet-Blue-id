from django import forms
from .models import User
class UserForm(forms.ModelForm):
    name_user = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class':'form-control',}))
    lastname_user = forms.CharField(label='Lastanme', widget=forms.TextInput(attrs={
        'class':'form-control',
    }))
    GENRE_CHOICES = [
        ('M','Masculin'),
        ('F','Feminin'),
        ('Autre','Autre'),
    ]
    sex_user  = forms.ChoiceField(label='sex', choices=GENRE_CHOICES ,widget=forms.TextInput(attrs={'class':'form-control',}))
    phone_user = forms.CharField(label='Phone', widget=forms.TextInput(attrs={'class':'form-control',}))
    date_user = forms.DateField(label='Date ', widget=forms.DateInput(
        attrs={'class':'form-control',}
    ))
    check_in_user = forms.TimeField(label='Check In', widget=forms.TimeInput(attrs={
        'class':'form-control',
    }))
    check_out_user = forms.TimeField(label='Check In', widget=forms.TimeInput(attrs={
        'class':'form-control',
    }))
    class Meta:
        model = User
        fields =('name_user' , 'lastname_user', 'phone_user',
                 'date_user', 'check_in_user','check_out_user' )
        
        
        
    
