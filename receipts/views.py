from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

from receipts.models import Receipt


def index(request):
	render(request, 'risiti/index.html')


class ReceiptIndexView(generic.ListView):
	queryset = Receipt.objects.order_by('-date_created')
	context_object_name = "receipt_list"
	template_name = "receipts/index.html"

class ReceiptDetailView(generic.DetailView):
	model = Receipt
	template_name = "receipts/detail.html"
