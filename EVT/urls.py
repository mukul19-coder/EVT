from django.contrib import admin
from django.urls import path, include

from home_view.views import home_view, signin_view, elastic_view, velcro_view, thread_view, log_out, shoppingcart_view, delete_item, checkout_view, order_1, order_view


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', home_view, name='home'),
    path('signin/', signin_view, name='signin'),
    path('elastic/', elastic_view, name='elastic'),
    path('shoppingcart/', shoppingcart_view, name='shoppingcart'),
    path('checkout/', checkout_view, name='checkout'),
    path('logout/', log_out, name='log_out'),
    path('velcro/', velcro_view, name='velcro'),
    path('deleteitem/', delete_item, name='deleteitem'),
    path('purchase/', order_1, name='purchase'),
    path('orders/', order_view, name='orders'),
    path('thread/', thread_view, name='thread'),
    path('admin/', admin.site.urls),
    path('Client/', include('Client.urls')),
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)