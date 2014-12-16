from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quiz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('game.urls')),
    url(r'^editor/', include('editor.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


