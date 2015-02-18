from django import forms

class EmailForm(forms.Form):
    your_email = forms.EmailField(label='Your email', max_length=100)

class ContactForm(forms.Form):
    your_feedback = forms.CharField(widget=forms.Textarea, label="")