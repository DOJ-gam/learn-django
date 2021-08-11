from django.urls import path
from . import views

urlpatterns = [
    # path('jan', views.jan),
    # path('feb', views.feb),
    # path('mar', views.mar),
    # path('apr', views.apr),
    # path('may', views.may),
    # path('jun', views.jun),
    # path('jul', views.jul),
    # path('aug', views.aug),
    # path('sep', views.sep),
    # path('oct', views.oct),
    # path('nov', views.nov),
    # path('dec', views.dec),
    # path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge),
]
