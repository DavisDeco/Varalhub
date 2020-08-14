
from django.urls import path, include
from django.contrib import admin
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('account', createAccount, name='my-account'),
    path('wishlist', wishlist, name='wishlist'),
    path('mycart', mycart, name='mycart'),
    path('checkout', checkout, name='checkout'),
    path('contact', contactus, name='contact'),

    # url to accounts/api 
    path('accounts/', include(('accounts.urls','accounts'), namespace='accounts')),

]
