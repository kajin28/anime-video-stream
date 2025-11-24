from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('index/', views.index, name='index'),
    path('animes/', views.anime_list, name='anime_list'),
    path('anime/<int:anime_id>/', views.anime_detail_view, name='anime_detail'),
    path('subscribe/', views.subscribe_view, name='subscribe'),
    path('payment/<int:plan_id>/', views.payment_view, name='payment'),
    path('payment/confirm/', views.payment_confirm, name='payment_confirm'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)