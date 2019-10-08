from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User
from django.contrib.auth.forms import  UsernameField, PasswordChangeForm

class NewRegistrationForm(UserCreationForm):
	email = forms.EmailField()
	username = forms.CharField(label="Loja", max_length=100)
	telefone = forms.CharField(label="Telefone", max_length=15)
	celular = forms.CharField(label="Celular", max_length=15)
	cidade = forms.CharField(label='Cidade', max_length=30)
	
	class Meta:
		model = User
		fields = ('email', 'username', 'telefone', 'celular', 'cidade')


class NewUserChangeForm(UserChangeForm):

	class Meta:
		model = User
		fields = ('username', 'email')


class form_de_mudar_dados(forms.ModelForm):
	"""email = forms.EmailField()
				username = forms.CharField(label="Loja", max_length=100)
				telefone = forms.CharField(label="Telefone", max_length=15)
				celular = forms.CharField(label="Celular", max_length=15)
				cidade = forms.CharField(label='Cidade', max_length=30)"""
	class Meta:
		model = User
		fields = ('email', 'telefone', 'celular', 'cidade')




		
"""class SetPasswordForm(forms.Form):
    """
   # A form that lets a user change set their password without entering the old
    #password
"""
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput,
        strip=False,
    )
    new_password2 = forms.CharField(
        label="New password confirmation",
        strip=False,
        widget=forms.PasswordInput,
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        password_validation.validate_password(password2, self.user)
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user


class PasswordChangeForm(SetPasswordForm):
    """
   # A form that lets a user change their password by entering their old
  #  password.
"""
    error_messages = dict(SetPasswordForm.error_messages, **{
        'password_incorrect':"Your old password was entered incorrectly. Please enter it again.",
    })
    old_password = forms.CharField(
        label="Old password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True}),
    )

    field_order = ['old_password', 'new_password1', 'new_password2']

    def clean_old_password(self):
        """
    #    Validate that the old_password field is correct.
"""
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password"""

class form_de_mudar_senha(PasswordChangeForm):
	old_password = forms.CharField(label="Senha Atual", widget=forms.PasswordInput)
	new_password1 = forms.CharField(label="Nova Senha", widget=forms.PasswordInput)
	new_password2 = forms.CharField(label="Confirmação da nova senha", widget=forms.PasswordInput)

	class Meta:
		model = User