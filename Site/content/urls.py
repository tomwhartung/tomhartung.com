""" urls.py for our content app

Purpose: define the urls for this app
Author: Tom W. Hartung
Date: Fall, 2018.
Copyright: (c) 2018 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
    https://docs.djangoproject.com/en/2.1/intro/tutorial01/#write-your-first-view
"""

from django.conf.urls import *

from . import views

"""
When upgrading to django 2.0+, we can use the path method:
    https://docs.djangoproject.com/en/2.0/ref/urls/#path

from django.urls import path

The routes we are using are quite simple, and we already have a
version of this file that uses the path method:
    ./urls-uses_path-save_for_2.0.py
More:
    https://stackoverflow.com/questions/47947673/is-it-better-to-use-path-or-url-in-urls-py-for-django-2-0
"""

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home$', views.home, name='home'),
    url(r'^about$', views.about, name='about'),
    url(r'^opinions$', views.opinions, name='opinions'),
    url(r'^v$', views.versions, name='versions'),
    url(r'^legal/affiliate_marketing_disclosure$',
        views.affiliate_marketing_disclosure,
        name='affiliate_marketing_disclosure'),
    url(r'^legal/privacy_policy$',
        views.privacy_policy,
        name='privacy_policy'),
    url(r'^legal/terms_of_service$',
        views.terms_of_service,
        name='terms_of_service'),
    url(r'^(?P<unknown_page>[\w\W]+)$',
        views.not_found,
        name='not_found'),
]
