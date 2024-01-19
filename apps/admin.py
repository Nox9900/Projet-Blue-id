from django.contrib import admin
from .models import  PersonalOffice , Employed , User

@admin.register(PersonalOffice)

class PersonalOfficeAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'
        
@admin.register(Employed)

class EmployedAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'
        
        
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'
