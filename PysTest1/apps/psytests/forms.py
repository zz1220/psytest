from django import forms

class ReviewForm(forms.Form):
    review = forms.CharField(label='review', max_length=100)
