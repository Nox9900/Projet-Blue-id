from django.shortcuts import render, redirect 
from .models import  PersonalOffice, User
from .forms import PersonalForm

def index(request):
    if request.method == "POST":
        add_form = UserForm(request.POST or None)
        if add_form.is_valid():
            fn = add_form.cleaned_data['name']
            ln = add_form.cleaned_data['lastname']
            sex = add_form.cleaned_data['sex']
            phone = add_form.cleaned_data['phone']
            User.objects.create(
                name = fn,
                lastname = ln,
                sex = sex,
                phone = phone,
            )

    list_user = User.objects.order_by('-id').all()
    list_number_users = list_user.count()
    message = f'{list_number_users} utilisateurs'
    if list_number_users == 1:
        message = f'{list_number_users} utilisateur'    
    context = {
        'user': User.objects.all(),
        'form': UserForm(),
        'users': list_user,
        'message': message,
        'list_number_users':list_number_users
    }
    return render(request, 'apps/index.html', context)


def list_personal_office(request):

    if request.method == "POST":

        add_form = PersonalForm(request.POST or None)
        

        if add_form:

            if add_form.is_valid():

                fn = add_form.cleaned_data['fristname']
                ln = add_form.cleaned_data['lastname']
                sex = add_form.cleaned_data['sex']
                phone = add_form.cleaned_data['phone']
                email = add_form.cleaned_data['email']

                PersonalOffice.objects.create(
                    fristname = fn,
                    lastname = ln,
                    sex = sex,
                    phone = phone,
                    email = email
                )

        
    context = {
        'personals': PersonalOffice.objects.all(),
        'add_form': PersonalForm(),
    }
    return render(request , 'apps/list_personal_office.html', context)


def show_personal(request, pk):

    personal = PersonalOffice.objects.get(id = pk)

    context = {
        'personal': personal,
    }

    return render(request, 'apps/show_personal_office.html', context)

def update_personal(request, pk):

    personal_to_edit = PersonalOffice.objects.get(id = pk)

    

    return redirect("apps:personal")

def remove_personal(request, pk):

    personal_to_remove = PersonalOffice.objects.get(id = pk)

    personal_to_remove.delete()

    return redirect("apps:personal")


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
     #pour la partie user list , remove , show
def list_users(request):
    if request.method == "POST":
        add_form = UserForm(request.POST or None)
        if add_form:
            if add_form.is_valid():
                fn = add_form.cleaned_data['name']
                ln = add_form.cleaned_data['lastname']
                sex = add_form.cleaned_data['sex']
                phone = add_form.cleaned_data['phone']
                User.objects.create(
                    name = fn,
                    lastname = ln,
                    sex = sex,
                    phone = phone,
                )

    list_user = User.objects.order_by('-id').all()
    list_number_users = list_user.count()
    message = f'{list_number_users} utilisateurs'
    if list_number_users == 1:
        message = f'{list_number_users} utilisateur'    
    context = {
        'user': User.objects.all(),
        'form': UserForm(),
        'users': list_user,
        'message': message,
        'list_number_users':list_number_users
    }
    return render(request , 'apps/list_user.html', context)

def remove_user(request , id_user):
    user = User.objects.get(id=id_user)
    user.delete()
    return redirect('apps:user')

def show_information_user(request , id_user):
    user = User.objects.get(id=id_user)
    context = {'user': user}
    return render(request , "apps/show_user.html",context)
