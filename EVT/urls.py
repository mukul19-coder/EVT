from django.contrib import admin
from django.urls import path, include

from home_view.views import home_view, success, paid, addquantity, delquantity, panel, outfordelivery, delivered, confirmorder, changeaddress, changeorgname, changepassword, changenumber, psettings, register, signin_view, elastic_view, velcro_view, thread_view, log_out, shoppingcart_view, delete_item, cancel_order, checkout_view, order_1, order_view

from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "EVT Administration"
admin.site.site_title = "EVT Administration"
admin.site.index_title = "Welcome to EVT"

urlpatterns = [
	path('', home_view, name='home'),
    path('signin/', signin_view, name='signin'),
    path('elastic/', elastic_view, name='elastic'),
    path('shoppingcart/', shoppingcart_view, name='shoppingcart'),
    path('checkout/', checkout_view, name='checkout'),
    path('logout/', log_out, name='log_out'),
    path('velcro/', velcro_view, name='velcro'),
    path('deleteitem/', delete_item, name='deleteitem'),
    path('cancelorder/', cancel_order, name='cancelorder'),
    path('confirmorder/', confirmorder, name='confirmorder'),
    path('success/', success, name='success'),
    path('outfordelivery/', outfordelivery, name='outfordelivery'),
    path('addquantity/', addquantity, name='addquantity'),
    path('delquantity/', delquantity, name='delquantity'),
    path('delivered/', delivered, name='delivered'),
    path('purchase/', order_1, name='purchase'),
    path('changepassword/', changepassword, name='changepassword'),
    path('paid/', paid, name='paid'),
    path('changeorgname/', changeorgname, name='changeorgname'),
    path('changeaddress/', changeaddress, name='changeaddress'),
    path('changenumber/', changenumber, name='changenumber'),
    path('register/', register, name='register'),
    path('orders/', order_view, name='orders'),
    path('settings/', psettings, name='settings'),
    path('panel/', panel, name='panel'),
    path('thread/', thread_view, name='thread'),
    path('admin/', admin.site.urls),
    path('Client/', include('Client.urls')),
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)