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

from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='my-login')
def createTask(request):
    # Check if the user is an admin
    if request.user.username == 'admin10':
        form = TaskForm()

        if request.method == "POST":
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.user = request.user
                task.save()
                messages.success(request, 'Task created successfully!')
                return redirect('view-tasks')
        context = {'form': form}
        return render(request, 'profile/create-task.html', context=context)
    else:
        # If the user is not 'admin10', redirect to the task-denied page
        messages.error(request, 'You are not authorized to create tasks.')
        return redirect('task-denied')  # Corrected redirection

def taskDenied(request):
    return render(request, 'task-denied.html')



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



from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskStatusForm

@login_required(login_url='my-login')
def updateTask(request, pk):
    task = get_object_or_404(Task, pk=pk)

    # Check if the logged-in user is assigned to the task or is an admin
    if request.user == task.assigned_to or request.user.username == 'admin10':
        if request.method == 'POST':
            form = TaskStatusForm(request.POST, instance=task)
            if form.is_valid():
                # Get the instance of the task with updated status only
                updated_task = form.save(commit=False)
                # Save only the status field and keep other fields unchanged
                task.status = updated_task.status
                task.save()
                messages.success(request, 'Task status updated successfully!')
                return redirect('view-tasks')
        else:
            form = TaskStatusForm(instance=task)
        return render(request, 'profile/update-task.html', {'form': form})
    else:
        # If the user is neither assigned to the task nor an admin, show an error message
        messages.error(request, 'You are not authorized to update this task.')
        return redirect('view-tasks')



from django.contrib.auth.decorators import login_required

@login_required(login_url='my-login')
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.user.username == 'admin10':
        if request.method == 'POST':
            task.delete()
            return redirect('view-tasks')
        else:
            context = {'object': task}
            return render(request, 'profile/delete-task.html', context=context)
    else:
        # If the user is not 'admin10', show a pop-up message
        return render(request, 'profile/access-denied.html')


def accessDenied(request):
    return render(request, 'access_denied.html')





from django.contrib.auth.models import User

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            else:
                form.save()
                messages.success(request, "User Registration was Successful")
                return redirect('my-login')
    context = {'form': form}
    return render(request, 'register.html', context=context)



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
    

   

from django.contrib.auth import logout

def user_logout(request):
    return render(request, 'logout.html')

