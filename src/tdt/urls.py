from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'tdt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'tdt.views.contact', name='contact'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', 'tdt.views.about', name='about'),
    url(r'^bc/', 'tdt.views.bc', name='bc'),
    url(r'^pt/', 'tdt.views.pt', name='pt'),
    url(r'^nutrition/', 'tdt.views.nutrition', name='nutrition'),
    url(r'^mt/', 'tdt.views.mt', name='mt'),
    url(r'^bjj/', 'tdt.views.bjj', name='bjj'),
    url(r'^training/', 'tdt.views.training', name='training'),



]
