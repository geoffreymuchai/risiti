from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from receipts import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'risiti.views.home', name='home'),
    # url(r'^risiti/', include('risiti.foo.urls')),
	url(r'^$', "receipts.views.index", name = 'index'),
	url(r'^account/$', views.AccountListView.as_view(), name="account_list"),
	url(r'^account/create/$', views.AccountCreateView.as_view(), name="account_create"),
	url(r'^category/$', views.CategoryListView.as_view(), name = 'category_list'),
	url(r'^category/create/$', views.CategoryCreateView.as_view(), name = 'category_create'),
	url(r'^merchant/$', views.MerchantListView.as_view(), name = 'merchant_list'),
	url(r'^merchant/create/$', views.MerchantCreateView.as_view(), name="merchant_create"),
	url(r'^receipt/create/$', views.PaymentCreateView.as_view(), name="payment_create"),
	url(r'^receipt/$', views.PaymentListView.as_view(), name="payment_list"),
	url(r'^receipt/text/$', views.ReceiptListView.as_view(), name="receipt_text"),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
