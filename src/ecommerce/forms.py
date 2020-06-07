from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class ContactForm(forms.Form):
    fullname  = forms.CharField(max_length=200,
            widget=
                forms.TextInput(attrs=
                                {"class" : "form-control","placeholder" : "Your Full Name"}))
    email  = forms.EmailField(max_length=200,
            widget=forms.TextInput(attrs=
                    {"class" : "form-control","placeholder" : "Your Email"}))
    content  = forms.CharField(max_length=200,
            widget=forms.Textarea(attrs=
                    {"class" : "form-control","placeholder" : "Your Message"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email Error")
        return email





class LoginForm(forms.Form):
    username = forms.CharField( widget=
                forms.TextInput(attrs=
                                {"class" : "form-control","placeholder" : "Your Full Name"}))
    password = forms.CharField( widget=
                forms.TextInput(attrs=
                                {"class" : "form-control","placeholder" : "Your Full Name"}))

class RegisterForm(forms.Form):
    username =  forms.CharField(widget=
                forms.TextInput(attrs=
                                {"class" : "form-control","placeholder" : "Your Full Name"}))
    email  = forms.EmailField(widget=
                forms.EmailInput(attrs=
                                {"class" : "form-control","placeholder" : "Your Full Name"}))
    password = forms.CharField(widget=
                forms.TextInput(attrs=
                                {"class" : "form-control","placeholder" : "Your Full Name"}))
    password2 = forms.CharField(widget=
                forms.TextInput(attrs=
                                {"class" : "form-control","placeholder" : "Your Full Name"}))


    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password !=  password2:
            raise forms.ValidationError("Password Error")
        return data