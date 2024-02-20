from django.shortcuts import render,redirect,HttpResponse
from .models import Task
from .forms import TaskForm,CreateUserForm,LoginForm,UpdateUserForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def home(request):


    return render(request,'home.html')

@login_required(login_url='my-login')
def createTask(request):
    form=TaskForm()

    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.user=request.user
            task.save()
            return redirect('view-tasks')
    context={'form':form}
    return render(request,'profile/create-task.html',context=context)


from django.contrib.auth.decorators import login_required

@login_required(login_url='my-login')
def viewTasks(request):
    if request.user.username == 'admin10':
        tasks = Task.objects.all()
    else:
        current_user = request.user
        tasks = Task.objects.filter(assigned_to=current_user)

    context = {'tasks': tasks}
    return render(request, 'profile/view-tasks.html', context=context)



@login_required(login_url='my-login')
def updateTask(request, pk):
   task=Task.objects.get(id=pk)
   form=TaskForm(instance=task)
   if request.method=='POST':
       form=TaskForm(request.POST,instance=task)
       if form.is_valid():
           form.save()
           return redirect('view-tasks')
   context={'form':form}
   return render(request,'profile/update-task.html',context=context)  
   
@login_required(login_url='my-login')
def deleteTask(request, pk):
    task=Task.objects.get(id=pk)
    if request.method=='POST':
          task.delete()
          return redirect('view-tasks')
          
    context={'object':task}
    return render(request,'profile/delete-task.html',context=context)

def register(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User Registration was Successfull")
            return redirect('my-login')
        
    context={'form':form}
    return render(request,'register.html',context=context)


def my_login(request):
    form=LoginForm
    if request.method=='POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
    context={'form':form}
    return render(request,'my-login.html',context=context)

@login_required(login_url='my-login')
def dashboard(request):
    return render (request,'profile/dashboard.html')


@login_required(login_url='my-login')
def profile_management(request):
    if request.method=='POST':
        user_form =UpdateUserForm(request.POST,instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('dashboard')

    user_form=UpdateUserForm(instance=request.user)
    context ={'user_form': user_form}
    return render(request,'profile/profile-management.html',context=context)


@login_required(login_url='my-login')
def deleteAccount(request):
    if request.method =='POST':
        deleteUser=User.objects.get(username=request.user)
        deleteUser.delete()
        return redirect('')
    return render(request,'profile/delete-account.html')
    

def user_logout(request):
     auth.logout(request)
     messages.success(request, 'You have been logged out successfully!')
     return redirect('my-login')
   


