from django import forms
from .models import PhoneBook

class QuestionForm(forms.Form):
    first_name = forms.CharField(widget = forms.TextInput(attrs={'size': '50'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs={'size': '50'}))
    phone_number = forms.CharField(widget = forms.TextInput(attrs={'size': '50'}))

    def save(self, d: dict):
        first_name = d['first_name']
        last_name = d['last_name']
        phone_number = d['phone_number']
        phonebook = PhoneBook(first_name = first_name, 
        last_name=last_name,
        phone_number=phone_number)
        phonebook.save()

        contacts = PhoneBook.objects.all()
        for c in contacts:
            print("===============")
            print("First name: ", c.first_name)
            print("Last name: ", c.last_name)
            print("Phone number: ", c.phone_number)