from .models import Movies
from django import forms
from django.contrib.auth.models import User

class VideoForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ('title', 'description', 'video_file', 'date')

        # if post_form.is_valid():
        #     postAdded = True
        #     instance = post_form.save(commit=False)
        #     instance.author = poster
        #     instance.save()
