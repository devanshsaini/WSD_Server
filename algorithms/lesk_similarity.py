# importing required packages
import nltk
import numpy as np
from nltk.corpus import wordnet, stopwords
#nltk.download('wordnet')
nltk.download('stopwords')

stopwords_en = set(stopwords.words('english'))


def tokenize(document: str, word: str) -> set:
    # obtaining tokens from the gloss
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(document)

    # removing stop words from tokens
    tokens = [token for token in tokens if token not in stopwords_en and token.isalpha()]

    # removing the word from the tokens
    tokens = [token for token in tokens if token != word]
    return set(tokens)


def simple_lesk(gloss: str, word: str):
    """":returns the sense most suited to the given word as per the Simple LESK Algorithm"""

    # converting everything to lowercase
    gloss = gloss.lower()
    word = word.lower()

    # obtaining tokens from the gloss
    gloss_tokens = tokenize(gloss, word)

    # calculating the word sense disambiguation using simple LESK
    synsets = wordnet.synsets(word)
    weights = [0] * len(synsets)
    N_t = len(synsets)
    N_w = {}

    # Creating the IDF Frequency column using Laplacian Scaling
    for gloss_token in gloss_tokens:
        N_w[gloss_token] = 1

        for sense in synsets:
            if gloss_token in sense.definition():
                N_w[gloss_token] += N_t
                continue

            for example in sense.examples():
                if gloss_token in example:
                    N_w[gloss_token] += N_t
                    break

    for index, sense in enumerate(synsets):
        # adding tokens from examples into the comparison set
        comparison = set()
        for example in sense.examples():
            for token in tokenize(example, word):
                comparison.add(token)

        # adding tokens from definition into the comparison set
        for token in tokenize(sense.definition(), word):
            comparison.add(token)

        # comparing the gloss tokens with comparison set
        for token in gloss_tokens:
            if token in comparison:
                weights[index] += np.log(N_w[token] / N_t)

    max_weight = max(weights)
    index = weights.index(max_weight)
    return synsets[index], weights
