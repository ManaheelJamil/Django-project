from django import forms

class usersForm(forms.Form):
    num1 = forms.IntegerField(label="Value1", required=True)
    num2 = forms.IntegerField(label="Value2", required=True)
