__author__ = 'Paul Fleischer'


from django.conf.urls import *


urlpatterns = patterns('',
        url(r'^$', 'public.views.home', name='home'),
        url(r'^helping/hand/$', 'public.views.helping_hand_lp', name='helping_hand_lp'),
        url(r'^purchase/(?P<id>\d+)?$', 'public.views.purchase_product', name='purchase'),
    )