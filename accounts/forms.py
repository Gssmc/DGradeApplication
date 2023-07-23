from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from .models import MyUser
 




class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        #fields = ('email', )
        fields = '__all__'
        exclude = ('is_active','is_admin','last_login','password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control','placeholder': 'Your name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control','placeholder': 'example@gmail.com'})
        self.fields['institution'].widget.attrs.update({'class': 'form-control','placeholder': 'Your Organization'})
        self.fields['contact'].widget.attrs.update({'class': 'form-control','placeholder': '+8801'})
        self.fields['account_type'].widget.attrs.update({'class': 'form-control','placeholder': 'Enter password'})
        self.fields['address'].widget.attrs.update({ 'rows':3, 'class': 'form-control','placeholder': '23/B Najrul Islam Avenue,Dhaka,Bangladesh'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control','placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control','placeholder': 'Re-password'})

        

        



    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'is_active', 'is_admin',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]



class LoginForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields=('email','password',)


 
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control','placeholder': 'example@gmail.com'})
        self.fields['password'].widget.attrs.update({'class': 'form-control','placeholder': 'Your password Here'})
      