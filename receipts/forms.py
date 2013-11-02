from django import forms
from receipts.models import Account

class AccountForm(forms.ModelForm):
	class Meta:
		model = Account
		fields = ['name', 'description', 'account_type', 'amount']