from django import forms
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = "__all__"  # если не все поля, то в других должно быть blank=True

