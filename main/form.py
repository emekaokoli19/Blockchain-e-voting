from django import forms

class CreateNewUser(forms.Form):
    name = forms.CharField(label="FULL NAME", max_length=200)
    PVC_no = forms.CharField(label="PVC NO", max_length=10)
    password = forms.CharField(label="PASSWORD", max_length=25)
    confirm_password = forms.CharField(label="CONFIRM PASSWORD", max_length=25)

class Login(forms.Form):
    vote_ID = forms.CharField(label="VOTE ID", max_length=20)
    password = forms.CharField(label="PASSWORD", max_length=25)