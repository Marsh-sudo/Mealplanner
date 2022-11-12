from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path('signup/', views.signup, name='signup'),
    path('login',views.login_request,name="login"),
    path("search/",views.search,name="search"),
    path("wines",views.wines,name="wines"),
    path("wineSearch/",views.wines_pairing,name="wineSearch")

]