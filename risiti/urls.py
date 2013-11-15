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
	url(r'^account/$', views.AccountListView.as_view(), name="account"),
	url(r'^account/create/$', views.AccountCreateView.as_view()),
	url(r'^category/$', views.CategoryListView.as_view()),
	url(r'^category/create/$', views.CategoryCreateView.as_view()),
	url(r'^merchant/$', views.MerchantListView.as_view()),
	url(r'^merchant/create/$', views.MerchantCreateView.as_view()),
	url(r'^receipt/create/$', views.ReceiptCreateView.as_view()),
	url(r'^receipt/$', views.ReceiptListView.as_view()),
	url(r'^receipt/text/$', views.ReceiptTextListView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
