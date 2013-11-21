from django import forms
from receipts.models import Account, Category, Merchant, Payment

class AccountForm(forms.ModelForm):
	class Meta:
		model = Account
		fields = ['name', 'description', 'account_type', 'amount']

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name', 'value']

class MerchantForm(forms.ModelForm):
	class Meta:
		model = Merchant
		fields = ['name', 'description', 'total_amount_debited']

class PaymentForm(forms.ModelForm):
	class Meta:
		model = Payment
		widgets = {
				"date":forms.TextInput(attrs={'id':'datepicker'})
			}
		fields = ['date', 'description', 'bought_from', 'category', 'account_to_credit', 'price', 'image']
