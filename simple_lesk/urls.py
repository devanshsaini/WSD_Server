from django.urls import path

from . import views

urlpatterns = [
    path('simple_lesk/<sentence>/<word>/', views.find_similarity, name='simeple_lesk_similarity'),
]