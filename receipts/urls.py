from django.conf.urls import patterns, url

from receipts import views

urlpatterns = patterns('',
	# url(r'^(?P<pk>\d+)/$', views.ReceiptDetailView.as_view(), name='detail')
	
	# url(r'^(?P<account_id>\d+)/$', views.AccountDetailView.as_view(), name='detail')
)
