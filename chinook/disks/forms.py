from django.db import forms

class AlbumForm(forms.ModelForm):
    class Meta:
    model = Album
    fields = '__all__'
