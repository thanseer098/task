from django import forms
from . models import Register
class Registerform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=Register                                         
        fields='__all__'
class Loginform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=Register                                         
        fields=('email','password',)
class UpdateForm(forms.ModelForm):
    class Meta():
        model=Register
        fields=('name','age','place','email')

class changepasswordform(forms.Form):
    oldpassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    newpassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    confirmpassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)        