import nltk
from nltk.corpus import wordnet, wordnet_ic
# nltk.download('wordnet')
# nltk.download('wordnet_ic')
# nltk.download('omw-1.4')
import numpy as np

# Defining Infinity
infinity = float('inf')

# Importing the Brown Corpus
brown_ic = wordnet_ic.ic('ic-brown.dat')


# Defining the Closest Synsets Function Based on Resnik Similarity Score
def closest_synsets(word_1: str, word_2: str):
    word_1 = wordnet.synsets(word_1)
    word_2 = wordnet.synsets(word_2)
    max_similarity = -infinity
    try:
        synset_1_shortest = word_1[0]
        synset_2_shortest = word_2[0]
    except:
        return None, None, -infinity

    for synset_1 in word_1:
        for synset_2 in word_2:
            if synset_1.pos() != synset_2.pos():
                continue
            similarity = synset_1.res_similarity(synset_2, ic=brown_ic)
            if similarity > max_similarity:
                max_similarity = similarity
                synset_1_shortest = synset_1
                synset_2_shortest = synset_2

    return synset_1_shortest, synset_2_shortest, max_similarity
