from django import forms


class CommandForm(forms.Form):
    command = forms.CharField(label='command', max_length=2000)
