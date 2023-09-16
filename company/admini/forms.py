from django import forms
from .models import User,Amodel


class Logins(forms.Form):
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={"placeholder":"username","class":"form-control"}))
    password=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={"placeholder":"password","class":"form-control"}))
    def clean(self):
        pswd=self.cleaned_data.get("password")
        if len(pswd)>8:
            msg="password is more than 8 character"
            self.add_error("password",msg)
        return super().clean()
    

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'username', 'password', 'gender', 'course', 'qualification', 'address']

class Aforms(forms.ModelForm):
    class Meta :
        model = Amodel
        fields=['name','email','age']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
        }
