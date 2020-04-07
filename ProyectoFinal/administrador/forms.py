from django import forms
class AdminForm(forms.ModelForm):
   	usuario = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:

        widgets = {
      		'password': forms.PasswordInput()
        }
