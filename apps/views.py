from django.shortcuts import render , redirect , get_object_or_404
from .models import  PersonalOffice, User
from .forms import UserForm
def index(request):
    
    return render(request , 'apps/index.html')


def list_personal_office(request):
    list_personal_office = PersonalOffice.objects.all()
    list_number_of_personal = list_personal_office.count()
    message = f'{list_number_of_personal} personnes'
    
    if list_number_of_personal == 1:
        message = f'{list_number_of_personal} personne'
        
    context = {
        'personals': list_personal_office,
        'message': message,
    }
    return render(request , 'apps/list_personal_office.html', context)
def list_users(request):
    list_user = User.objects.all()
    
    list_number_users = list_user.count()
    message = f'{list_number_users} utilisateurs'
    
    if list_number_users == 1:
        message = f'{list_number_users} utilisateur'
        
    context = {
        'users': list_user,
        'message': message,
        'list_number_users':list_number_users
    }
    return render(request , 'apps/list_user.html', context)
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST )
        if form.is_valid():
            form = form.save()
            form.user = request.user
            form.save()
            return redirect('apps:main')
    else:
        form = UserForm()
    
    context ={
        'forms':form
    }
    return render(request , 'apps/add_user.html' , context)

def main(request):
    return render(request , 'apps/main.html')
