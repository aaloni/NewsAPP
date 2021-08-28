from django.core.validators import RegexValidator
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User= get_user_model()

YEARS= [x for x in range(1940,2021)]

# Registration form with requested fields
class NewUserForm(UserCreationForm):

	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

	#Regular expression for phone number
	phone_regex = RegexValidator(regex=r'^\+?966?\d{9,13}$')
	phone = forms.CharField(help_text='+966xxxxxxxxx',validators=[phone_regex], max_length=100)
	national_id = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
	birth_date = forms.DateField(label='Birth date', widget=forms.SelectDateWidget(years=YEARS))


	class Meta:
		model = User
		fields = ("first_name","last_name","phone","username", "email", "password1", "password2","national_id","birth_date",)

	#Commit new user
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']

		if commit:
			user.save()
		return user