from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import CreateView

from receipts.models import Receipt, ReceiptText, Account, Category, Merchant
from receipts.forms import AccountForm, CategoryForm, MerchantForm, ReceiptForm

def index(request):
	return render(request, 'risiti/index.html')

class ReceiptCreateView(CreateView):
	form_class = ReceiptForm
	model = Receipt
	template_name = "risiti/base_form.html"
	success_url = '/receipt/'


class ReceiptListView(generic.ListView):
	queryset = Receipt.objects.order_by('-date_created')
	context_object_name = "receipt_list"
	template_name = "risiti/receipt_list.html"

class ReceiptTextListView(generic.ListView):
	queryset = ReceiptText.objects.order_by('-date_created')
	context_object_name = "receipt_text_list"
	template_name = "risiti/base_list.html"

class ReceiptDetailView(generic.DetailView):
	model = Receipt
	template_name = "risiti/receipts_detail.html"


class AccountListView(generic.ListView):
	model = Account
	context_object_name = "account_list"
	template_name = "risiti/base_list.html"

class AccountCreateView(CreateView):
	form_class = AccountForm
	model = Account
	template_name = "risiti/base_form.html"
	success_url = '/account/'

class CategoryCreateView(CreateView):
	form_class = CategoryForm
	model = Category
	template_name = "risiti/base_form.html"
	success_url = '/category/'

class CategoryListView(generic.ListView):
	model = Category
	context_object_name = "category_list"
	template_name = "risiti/base_list.html"

class MerchantCreateView(CreateView):
	form_class = MerchantForm
	model = Merchant
	template_name = "risiti/base_form.html"
	success_url = '/merchant/'

class MerchantListView(generic.ListView):
	model = Merchant
	context_object_name = "merchant_list"
	template_name = "risiti/base_list.html"