from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from user import views

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
    path('create_user/', views.NewUserView.as_view()),
    path('get_phases/', views.get_phases, name="phase"),
    path('provinsi/', views.provinsi_list, name="provinsi"),
    path('kabupaten/<provinsi_id>/', views.kabupaten_list, name="kabupaten"),
    path('kecamatan/<kabupaten_id>/', views.kecamatan_list, name="kecamatan"),
    path('kelurahan/<kecamatan_id>/', views.kelurahan_list, name="kelurahan"),
]
