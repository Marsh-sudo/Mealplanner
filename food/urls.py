from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from food.views import ChangePasswordView

urlpatterns=[
    path("",views.home,name="home"),
    path('signup/', views.signup, name='signup'),
    path('login',views.login_request,name="login"),
    path('profile/', views.profile, name='users-profile'),
    path("logout", views.logout_request, name= "logout"),
    path("search/",views.search,name="search"),
    path("wines",views.wines,name="wines"),
    path("wineSearch/",views.wines_pairing,name="wineSearch"),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)