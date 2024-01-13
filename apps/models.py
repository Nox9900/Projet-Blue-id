from django.db import models

class PersonalOffice(models.Model):
    name_personal = models.CharField(max_length=100)
    lastname_personal = models.CharField(max_length=100)
    SEX_TYPES = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )
    sex_personal = models.CharField(max_length=1 , choices = SEX_TYPES)
    phone_personal = models.CharField(max_length=50)
    email_personal = models.EmailField(max_length=255)
    # check_in_personal = models.DateTimeField(auto_now_add=True)
    # check_out_personal = models.DateTimeField(null=True , blank=True)
    # date_personal = models.DateField(auto_now_add=False)
    class Meta : 
        verbose_name = 'personnel du bureau'
        
        def __str(self):
            return f'{self.name_personal} {self.lastname_personal} {self.phone_personal} {self.date_personal}'
        
        
class Employed (models.Model):
    name_employed = models.CharField(max_length=255)
    lastname_employed = models.CharField(max_length=200)
    phone_employed = models.CharField(max_length=255)
    SEX_TYPES = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )
    sex_employed = models.CharField(max_length=1 , choices = SEX_TYPES)
    SERVICE_TYPES = (
       
        ('HDTT', 'Hopital de Tié Tié'),
        ('HDP', 'Hopital de PATRA'),
    )
    service_employed = models.CharField(max_length=10 , choices = SERVICE_TYPES)
    check_in_employed = models.DateTimeField(auto_now_add=True)
    check_out_employed = models.DateTimeField(null=True , blank=True)
    # date_employed = models.DateField(auto_now_add=False)
    
    class Meta:
        verbose_name = 'Employé'
        verbose_name_plural ='employés'
        
        def __str__(self):
            return f'{self.name_employed} {self.lastname_employed} {self.phone_employed} {self.date_employed}'
        
class User(models.Model):
    name_user = models.CharField(max_length=100)
    lastname_user = models.CharField(max_length=100)
    SEX_TYPES = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )
    sex_user = models.CharField(max_length=1 , choices = SEX_TYPES)
    phone_user = models.CharField(max_length=50)
    email_user = models.EmailField(max_length=255)
    check_in_user = models.TimeField(auto_now_add=False)
    check_out_user = models.TimeField(null=True , blank=True)
    date_user = models.DateField(auto_now_add=False)
    class Meta : 
        verbose_name = 'utilisateur'
        
        def __str(self):
            return f'{self.name_user} {self.lastname_user} {self.phone_user} {self.date_user} {self.check_in_user} {self.check_out_user}'
