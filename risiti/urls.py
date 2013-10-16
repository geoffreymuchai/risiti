from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'risiti.views.home', name='home'),
    # url(r'^risiti/', include('risiti.foo.urls')),
	url(r'^$', 'risiti.views.templates.index', name="index"),
	url(r'^receipt/', include('receipts.urls', namespace='receipt')),
    url(r'^admin/', include(admin.site.urls)),
)
