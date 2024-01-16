from typing import Any
from django.db import models

class AbstractEntity(models.Model):
    fristname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    SEX_TYPES = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )
    sex = models.CharField(max_length=1 , choices = SEX_TYPES)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique = True)
    date = models.DateField(auto_now_add=True)
    #check_in = models.DateTimeField(auto_now_add=True)
    # check_out_personal = models.DateTimeField(null=True , blank=True)


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
            return f'{self.firstname} {self.lastname} {self.phone} {self.date}'
