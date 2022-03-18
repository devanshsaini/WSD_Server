from django.http import JsonResponse
from algorithms.simple_lesk import simple_lesk


def find_similarity(request, sentence, word):
    words = simple_lesk(sentence, word)
    return JsonResponse({
        'sense': words['sense'].definition(),
        'weights': words['weights']
    })