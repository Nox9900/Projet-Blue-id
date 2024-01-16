from typing import Any
from django.db import models

class AbstractEntity(models.Model):
    name =models.CharField(max_length=250)
    lastname =models.CharField(max_length=250)
    email =models.EmailField(max_length=250)
    phone =models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    SEX_TYPES = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )
    sex = models.CharField(max_length=1 , choices = SEX_TYPES)

class PersonalOffice(AbstractEntity):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    class Meta : 
        verbose_name = 'personnel du bureau'
        
        def __str__(self):
            return f'{self.firstname} {self.lastname} {self.phone} {self.date}'
        
        
class Employed (AbstractEntity):

    SERVICE_TYPES = (
       
        ('HDTT', 'Hopital de Tié Tié'),
        ('HDP', 'Hopital de PATRA'),
    )

    service_employed = models.CharField(max_length=10 , choices = SERVICE_TYPES)
 
    class Meta:
        verbose_name = 'Employé'
        verbose_name_plural ='employés'
        
        def __str__(self):
            return f'{self.firstname} {self.lastname} {self.phone} {self.date}'
class User(AbstractEntity):
    class Meta : 
        verbose_name = 'utilisateur'
        def __str(self):
            return f'{self.name} {self.lastname} {self.phone} {self.date} {self.time}'
