from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
	(r'^polls/$', 'polls.views.index'),
	(r'^polls/(\d+)/$', 'polls.views.detail'),
	(r'^polls/(\d+)/results/$', 'polls.views.results'),
	(r'^polls/(\d+)/vote/$', 'polls.views.vote'),
)
