from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from receipts import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'risiti.views.home', name='home'),
    # url(r'^risiti/', include('risiti.foo.urls')),
	url(r'^$', "receipts.views.index", name = 'index'),
	url(r'^account/$', views.AccountListView.as_view(), name="account"),
	url(r'^account/create/$', views.AccountCreateView.as_view()),
	url(r'^category/create/$', views.CategoryCreateView.as_view()),
	url(r'^merchant/create/$', views.MerchantCreateView.as_view()),
	url(r'^receipt/create/$', views.ReceiptCreateView.as_view()),
	url(r'^receipt/$', include('receipts.urls', namespace='receipt')),
    url(r'^admin/', include(admin.site.urls)),
)
