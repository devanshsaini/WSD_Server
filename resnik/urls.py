from django.urls import path

from . import views

urlpatterns = [
    path('resnik/perform-similarity/<first_word>/<second_word>/', views.find_similarity, name='finding_similarity_between_words'),
]