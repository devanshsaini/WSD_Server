from django.http import JsonResponse
from algorithms.resnik_similarity import closest_synsets


def find_similarity(request, first_word, second_word):
    words = closest_synsets(first_word, second_word)
    print(words)
    return JsonResponse({
        'definition1': words[0].definition(),
        'definition2': words[1].definition(),
        'similarity': words[2]
    })