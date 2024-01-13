from django.contrib import admin
from .models import  PersonalOffice , Employed , User

@admin.register(PersonalOffice)

class PersonalOfficeAdmin(admin.ModelAdmin):
    list_display =('name_personal', 'lastname_personal', 'sex_personal', 'phone_personal')
    class Meta:
        fields = '__all__'
        
@admin.register(Employed)

class EmployedAdmin(admin.ModelAdmin):
    list_display = ('name_employed','lastname_employed','phone_employed','sex_employed','service_employed')
    
    class Meta:
        fields = '__all__'
        
        
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display =('name_user', 'lastname_user', 'sex_user', 'phone_user')
    class Meta:
        fields = '__all__'
