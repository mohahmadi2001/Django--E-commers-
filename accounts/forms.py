from django import forms
from accounts.models import User,OtpCode
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationsForm(forms.ModelForm):
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('email','phone_number','full_name')
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('password dont match')
        return cd['password2']
    
    def save(self, commit:True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user
    

class UserChangesForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="you can change your password in <a href=\"../password/\">this form</a>"
    )
    
    class Meta:
        model = User
        fields = ('email','phone_number','full_name','password')
        
        
class UserRegistrationForm(forms.Form):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=11, required=True)
    full_name = forms.CharField(label="full name", required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    def clean_email(self):
        email = self.cleaned_data['email']
        user =User.objects.filter(email=email).exists()
        if user:
            raise ValueError("email already exists")
        return email
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        user = User.objects.filter(phone_number=phone_number).exists()
        if user:
            raise ValueError("phone_number already exists")
        OtpCode.objects.filter(phone_number=phone_number).delete()
        return phone_number

class VerifyCodeForm(forms.Form):
    code = forms.IntegerField()
    


class UserLoginForm(forms.Form):
	phone_number = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)