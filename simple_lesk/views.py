from django.http import JsonResponse
from algorithms.lesk_similarity import simple_lesk


def simple_lesk_disambiguation(request, first_word, second_word):
    words = simple_lesk(first_word, second_word)
    print(words)
    return JsonResponse({
        'definition1': words[0].definition(),
        'definition2': words[1].definition(),
        'similarity': words[2]
    })