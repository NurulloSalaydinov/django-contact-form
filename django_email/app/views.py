from django.core.mail import send_mail
from django.shortcuts import render, redirect

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    contact_id = forms.CharField(widget=forms.Textarea)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print('Form is valid')
            
            send_mail('The contact form subject', 'This is the message', 'timforanalytics@gmail.com', ['salaydinovnurullo@gmail.com'])
            
            return redirect('/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
