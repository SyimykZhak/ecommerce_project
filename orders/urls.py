from django.urls import re_path as url
from . import views

app_name = "orders"
urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^admin/orders/order/(?P<order_id>\d+)/$', views.admin_order_detail, name='admin_order_detail'),
]