from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Task
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from dal import autocomplete


class UserSignUpForm(UserCreationForm):
    #image = forms.ImageField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]
    
    
class UserSigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput , required=False)
    

class ImageUploadForm(forms.Form):
    image = forms.ImageField()


class AssignTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description', 'due_date','priority','assignee']
        widgets = {
            'due_date': forms.DateInput(attrs={'class':'datepicker'}),
        }

# class AssignTaskForm(forms.Form):
#     title = forms.CharField(max_length= 100, required=True)
#     description = forms.CharField(required=False)
#     due_date = forms.DateField(required=True)
#     priority_choices = [('1','high'),('2','medium'),('3','low')] 
#     priority = forms.CharField(max_length=10, required=False)
#     assignees = forms.CharField(max_length= 100 , required=True, widget=forms.TextInput(
#         attrs={
#             'style': 'width: 400px',
#             'class': 'basicAutoComplete',
#             'data-url': "http://127.0.0.1:8005/assignee_autocomp/"
#         }))
    
#     def clean(self):
#         cleaned_data = super(AssignTaskForm, self).clean()
#         title = cleaned_data.get('title')
#         description = cleaned_data.get('description')
#         due_date = cleaned_data.get('due_date')
#         priority = cleaned_data.get('priority')
#         assignee = cleaned_data.get('assignees')
#         if not title and not assignee:
#             raise forms.ValidationError('You have to write something!')


