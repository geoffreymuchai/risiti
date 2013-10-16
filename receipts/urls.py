from django.conf.urls import patterns, url

from receipts import views

urlpatterns = patterns('',
	url(r'^$', views.ReceiptsIndexView.as_view(), name = 'index'),
	url(r'^(?P<pk>\d+)/$', views.ReceiptDetailView.as_view(), name='detail')
)
