from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'jobs.views.index', name='index'),

    # Job
    url(r'^job/add/$', 'jobs.views.add_job', name='add-job'),
    url(r'^job/edit/(\d+)/$', 'jobs.views.edit_job', name='edit-job'),
    url(r'^job/(\d+)/note/$', 'jobs.views.add_note', name='add-note'),

    # Django admin
    url(r'^admin/', include(admin.site.urls)),

    # Login/Logout
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'jobs/login.html'}, name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),

)
