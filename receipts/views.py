from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

from receipts.models import Receipt, Account, Category, Merchant


def index(request):
	return render(request, 'risiti/index.html')


class ReceiptListView(generic.ListView):
	queryset = Receipt.objects.order_by('-date_created')
	context_object_name = "receipt_list"
	template_name = "risiti/receipt_list.html"

class ReceiptDetailView(generic.DetailView):
	model = Receipt
	template_name = "risiti/receipts_detail.html"


class AccountListView(generic.ListView):
	model = Account
	context_object_name = "account_list"
	template_name = "risiti/account_list.html"
