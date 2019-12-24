from django import forms
from main.models import PostModel
class HomeForm(forms.ModelForm):
    post=forms.CharField()
    class Meta:
        model=PostModel
        fields=('post',)