from django import forms

class NameForm(forms.Form):
	firstname = forms.CharField(label="First Name", max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'first name' }))
	surname = forms.CharField(label="Surname", max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'surname' }))