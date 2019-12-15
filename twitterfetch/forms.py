from django import forms

class HashtagForm(forms.ModelForm):
  text = forms.CharField(label='Hashtag', max_length=100)