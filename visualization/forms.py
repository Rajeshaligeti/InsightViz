from django import forms

class UploadFileForm(forms.Form):
     file = forms.FileField(label="Choose an Excel/CSV file")
