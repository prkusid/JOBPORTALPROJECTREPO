from django import forms
from django.contrib.auth.models import User
from jobapp.models import Apply
class Register(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    cpassword = forms.CharField(widget=forms.PasswordInput,label = 'Confirm Password')
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username',]

    def clean(self):
        all_data = super().clean()
        pwd = all_data['password']
        cpwd = all_data['cpassword']
        if pwd != cpwd:
            raise forms.ValidationError('both password must be same')
