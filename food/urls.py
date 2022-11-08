from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("search/",views.search,name="search"),
    path("wines",views.wines,name="wines"),
    path("wineSearch/",views.wines_pairing,name="wineSearch")

]