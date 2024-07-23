from django import forms


class InfoForm(forms.Form):
    phone_number = forms.CharField(max_length=11, min_length=10)
    address = forms.CharField(max_length=200, min_length=2)
    name = forms.CharField(max_length=200, min_length=2)
    position = forms.CharField(max_length=200, min_length=2)
    sOrb = forms.CharField(max_length=6, min_length=5)
    file_license = forms.FileField()
