from django.urls import path

from . import views

urlpatterns = [
    path('simple_lesk/<first_word>/<second_word>/', views.simple_lesk_disambiguation, name='finding_similarity_between_words'),
]