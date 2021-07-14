import numpy as np
from map import *

def tokenize_text(text):
    # tagRe = re.compile(r'\\x.*?(2)')
    # normalText = tagRe.sub('', text)
    normalText = str(text)

    delete_list = ["-", "—", ",", ":", "?", "&", ";", "'", "\n", "\"", "!", "(", ")", "[", "]"]
    normalText = normalText.replace('Mr.', "Mr ")
    for s in delete_list:
        normalText = normalText.replace(s, '')

    normalText = normalText.replace(u'\xa0', u' ')
    phrases = normalText.lower().split(".")

    for i in range(len(phrases)):
        phrases[i] = phrases[i].replace("  ", '')

    return phrases

def define_parameters(phrases):
    transition_matrix = np.zeros((26,26))
    initial_state = np.zeros(26)

    for idp, phrase in enumerate(phrases):
        for idw, word in enumerate(phrase.split(' ')[1:]):

            if ord(word[0]) < ord('z') and ord(word[0]) > ord('a'):
                index = ord(word[0]) - 97
                initial_state[index] += 1
                a_ = ord(word[0]) - 97
                if len(word) > 1:
                    c_ = ord(word[1]) - 97
                transition_matrix[a_][c_] += 1
                for idc, char in enumerate(word[1:]):
                    a_ = ord(word[idc]) - 97
                    c_ = ord(word[idc + 1]) - 97
                    transition_matrix[a_][c_] += 1

    for i in range(len(transition_matrix)):
        transition_matrix[i] = (transition_matrix[i] + 1)/(transition_matrix[i].sum() + 26)

    for i in range(len(initial_state)):
        initial_state[i] += 1/26

    initial_state = initial_state / initial_state.sum()

    return transition_matrix, initial_state


def prob_word(word, transition_matrix, initial_state):
    p = np.log(initial_state[ord(word[0]) - 97])
    for idc, char in enumerate(word[1:]):
        a_ = ord(word[idc]) - 97
        c_ = ord(word[idc + 1]) - 97
        p = p + np.log(transition_matrix[a_][c_])

    return p


def prob_phrase(phrase, transition_matrix, initial_state):
    p = 0
    for idw, word in enumerate(phrase.split(' ')):
        a_ = prob_word(word, transition_matrix, initial_state)
        p = p + a_
    return p

def likelihood(dnas, text, transition_matrix, initial_state):
    results = []
    for i in range(len(dnas)):
        decoded = decode(text, dnas[i])
        results.append({'dna': dnas[i], 'result': prob_phrase(decoded, transition_matrix, initial_state)})

    return results