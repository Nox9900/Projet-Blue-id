from django import forms
from .models import PersonalOffice

class PersonalForm(forms.ModelForm):

    class Meta:
        model = PersonalOffice
        fields = [
            "fristname", 
            "lastname",
            "sex",
            "phone",
            "email"
        ]
        widgets = { 
            'fristname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name',
                'required': True, 
                } ),
            'lastname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name',
                'required': True, 
                } ),
            'phone' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Addresse email',
                'required': True, 
                } )
        }
    
