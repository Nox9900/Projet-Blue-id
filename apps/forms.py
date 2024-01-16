from django import forms
from .models import PersonalOffice , User

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
    
class UserForm(forms.Form):
    name =forms.CharField(max_length=255, required=True  , widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastname = forms.CharField(max_length=255, required=True , widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=255, required=True , widget=forms.TextInput(attrs={'class': 'form-control'}))
    GENRES_SEX = [('F','Femine'), ('M', 'Male'), ('Another', 'Another')]
    sex  = forms.ChoiceField(choices=GENRES_SEX , required=True,widget=forms.Select(attrs={'class': 'form-select'}))
    # date = forms.DateTimeField( required=True ,widget=forms.SelectDateWidget(attrs={'class':'form-control'},empty_label=('Choice your date')),
    #                                                                                  input_formats = ['%Y-%m-%d'])
    # check_in =forms.DateTimeField(
    #     widget=forms.DateTimeInput(attrs={'type': 'time',
    #                                       'class' : 'form-control'})
    # )
    class Meta:
        model = User
        fields = ['name' , 'lastname' , 'phone', 'sexe' , 'date' , 'time']
