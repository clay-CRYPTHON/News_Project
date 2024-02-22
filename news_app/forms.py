from django import forms
from .models import Contact, Comment

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"

class SubscriberForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']