from django import forms

class MyForm(forms.Form):
    uname =forms.CharField(label="Username",max_length=50)
    Password=forms.CharField(label="Password",widget=forms.PasswordInput())
    Pnumber = forms.CharField(label="Phone Number", max_length=10)
    Address= forms.CharField(label="Address", max_length=500)


