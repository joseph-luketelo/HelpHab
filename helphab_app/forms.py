from django import forms
from .models import Subscriber
from django.contrib.auth.forms import UserCreationForm


class SubscriberForm(forms.Form):
    first_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class':'form-control'})
    )
    last_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class':'form-control'})
    )
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={'class':'form-control'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password1 = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
    password2 = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
    address_one = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    address_two = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    city = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    state = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'})
    )


class LoginForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'})
    )


class QuestionsForm(forms.Form):
    TYPE_LIST = (
        (1, 'ASAP'),
        (2, 'TODAY'),
        (3, 'TOMORROW'),
        (4, 'END WEEK'),
        (5, 'NEXT WEEK'),
        (6, 'Other'),
    )
    question_title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'})
    )
    question_details = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control'})
    )
    budget = forms.IntegerField(label= 'Budget(USD)', required=False, widget=forms.TextInput(attrs={'class':'form-control'})
    )
    field = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'})
    )
    deadline = forms.ChoiceField(choices=TYPE_LIST)
    email_address = forms.EmailField(
        required=True, label='Valid email address(to be used by tutors for communication)', widget=forms.TextInput(attrs={'class':'form-control'})
    )
    # upload_files = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))


class HomeForm(forms.Form):
    pass
