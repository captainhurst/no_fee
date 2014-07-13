from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "id":"subject", "placeholder":"Subject"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "rows": "3", "id":"message", "placeholder":"Input your message..."}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={"type":"email", "class":"form-control", "id":"email-address", "placeholder":"Enter Email"}))
    #cc_myself = forms.BooleanField(required=False)