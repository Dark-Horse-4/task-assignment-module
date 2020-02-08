from django.shortcuts import render, redirect,reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, JsonResponse 
from .forms import UserSignUpForm ,UserSigninForm , ImageUploadForm, AssignTaskForm
from django.views.generic import TemplateView , ListView, CreateView
from django.contrib.auth import authenticate, login
from .models import Task , UserImage
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .filters import AssigneeFilter
from dal import autocomplete
#from .bg_task import mail_notifcation
from datetime import date, timedelta, datetime
from django.core.mail import send_mail
import datetime
import pdb
#from todo_app.tasks import notify_user
#from background_task import background
from django.contrib.auth.models import User
from .tasks import mailer


def HomeView(request):
    context ={
        'tasks': Task.objects.filter(assignee  = request.user.id) 
    }
    
    return render(request, 'todo_view/home.html', context)

def SignUp(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            #userimage = UserImage(user=userObject, image=form.cleaned_data('image'))
            #userimage.save()
            usermail = form.cleaned_data.get('email')
            #print(useremail)
            #mail_notifcation(usermail)
            # send_mail('verification', 'Sign up message.', 'sivaramelumalai4032588@gmail.com', [useremail], fail_silently=False)
            form.save(commit=True)
            return redirect('home')
    else:
        form = UserSignUpForm()
    return render(request, 'todo_view/sign-up.html', {'form': form})


class SignInView(TemplateView):
    def get (self, *args, **kwargs ):
        form =  UserSigninForm()
        return render(self.request , 'todo_view/sign-in.html', {'form': form} )
    
    def post(self, *args, **kwargs):
        form = UserSigninForm(self.request.POST)
        if form.is_valid():
            user = authenticate(username= form.cleaned_data['username'],
                                password= form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(self.request, user)
                    return HttpResponseRedirect(reverse('home'))
            else:
                return render(self.request , 'todo_view/sign-in.html', 
                              {'message':'incorrect credential','form':form })
        
        else:
            return render(self.request , 'todo_view/sign-in.html')
        
        
class TaskCreateView(CreateView):
    model = Task
    fields = ['title','description','assignee','due_date','priority']
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        Subject= 'New task assigned'
        date = str(self.request.POST.get('due_date')) 
        name = self.request.user.username
        Content = 'You have been assigned with the new task by '+name+'.The Due date to complete this is' + date
        send_mail(Subject, Content, 'sivaramelumalai4032588@gmail.com', ['sivaramelumalai4032588@gmail.com'], fail_silently=False)
        return super(TaskCreateView, self).dispatch(*args, **kwargs)

# def get_Assignee(request):
#     if request.user.is_authenticated:
#         q = request.GET.get('term','')
#         qs = User.objects.filter(username__istartswith= q)
#         result = []
#         for q in qs:
#             json = {}
#             json['id'] = q.id
#             json['text'] = q.username
#             result.append(json)
#             data = json.dumps(result)
#     else:
#         data ='fail'
#         mimetype = 'application/json'
#     return HttpResponse(data, mimetype)
    
    
# # def assignee_autocomplete(request):
# #     if request.GET.get('q'):
# #         q = request.GET['q']
# #         data = User.objects.using('legacy').filter(username__startswith=q).values_list('username',flat=True)
# #         json = list(data)
# #         return JsonResponse(json, safe=False)
# #     else:
# #         HttpResponse("No cookies")
 

# def NewTask(request):
#     if request.method == 'POST':
#         form = AssignTaskForm(request.POST)
#         if form.is_valid():
#             form.save(commit = False)
#             #a = Task(user = request.userObject , assignee = form.cleaned_data.get('assignees'))
#             #a.save()
#             form.save(commit = True)
#     else:
#         form  = AssignTaskForm()
#     return render(request, 'todo_view/task_form.html', {'form': form})


def UploadPic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            user = User.objects.get(pk=request.user.id)
            m = UserImage.objects.create(user=user, image=request.FILES['image'])
            m.save()
        return  HttpResponseRedirect(reverse('home'))
    
    else:
        form = ImageUploadForm()
        return render(request, 'todo_view/img-upload.html', {'form': form})


def MyTaskList(request):
    if request.user.is_authenticated:
        context ={
            'tasks': Task.objects.filter(assignee  = request.user.id) 
        }
        pdb.set_trace()
        mailer.delay('finish the task','task notification', ['sivaramelumalai4032588@gmail.com'],str(request.user.id))
        return render(request, 'todo_view/my-task.html', context)
    else:
        return render(request, 'todo_view/please-signin.html')
    
def send_email_to_user(request):
    	if request.user:
		    mailer.delay('finish the task','task notification', ['sivaramelumalai4032588@gmail.com'],frommail)


def CompletedTaskList(request, id):
    if request.user.is_authenticated:
        todo = Task.objects.get(id = id)
        todo.is_completed = True
        todo.save()
        context ={
            'tasks': Task.objects.filter(is_completed = True, assignee  = request.user.id) 
        }
        return render(request, 'todo_view/completed-task.html', context)
    else:
        return render(request, 'todo_view/please-signin.html')


def CompletedList(request):
    if request.user.is_authenticated:
        context ={
            'tasks': Task.objects.filter(is_completed = True, assignee  = request.user.id) 
        }
        return render(request, 'todo_view/completed-task.html', context)
    else:
        return render(request, 'todo_view/please-signin.html')


def UserTaskList(request , id):
        context ={
            'tasks': Task.objects.filter(is_completed = False, assignee  = id) 
        }
        return render(request, 'todo_view/home.html', context)



        
    
    


    

        
