from django import forms

class SteamIdForm(forms.Form):
    steamIdInput = forms.CharField(label='steamIdInput', max_length=30)