import random
import numpy as np
def encode(text, dict_map):
    new_text = ''
    for i in range(len(text)):
        if text[i] != ' ':
            new_text += dict_map[text[i]]
        else:
            new_text += ' '

    return new_text

def decode(text, dict_map):
    new_text = ''
    for i in range(len(text)):
        if text[i] != ' ':
            k = list(dict_map.values()).index(text[i])
            new_text += list(dict_map.keys())[k]
        else:
            new_text += ' '

    return new_text

def generate_dna(n):
    s1 = 'abcdefghijklmnopqrstuvwxyz'
    s2 = list(s1).copy()
    np.random.shuffle(s2)
    dicts = []
    for _ in range(n):
        dict = {}
        for i in range(len(s1)):
            dict.update({s1[i]: s2[i]})
        dicts.append(dict)

    return dicts

def generate_samples(dnas, n):
    dna_sequences = []
    for i in range(len(dnas)):
        dna_sequences.append(dnas[i])
        for j in range(n):
            dna = dnas[i].copy()
            k, p = random.sample(list(np.arange(len(list(dnas[i].keys())))), 2)
            dna[list(dna.keys())[k]], dna[list(dna.keys())[p]] = dna[list(dna.keys())[p]], dna[list(dna.keys())[k]]
            dna_sequences.append(dna)

    return dna_sequences