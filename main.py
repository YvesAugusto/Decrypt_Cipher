from utils import *
from map import *

def train(dnas, text):
    for _ in range(250):
        dnas = generate_samples(dnas, 3)
        log_likelihood = likelihood(dnas, text, transition_matrix, initial_state)

        best_results = sorted(
            log_likelihood, key = lambda x: x['result'],
            reverse=True
        )[0:5]

        sum = 0
        for i in range(len(best_results)):
            sum += best_results[i]['result']

        sum /= len(best_results)

        if _ % 50 == 0:
            print(f'[Epoch {_}] - Mean log-likelihood: {sum}')

        dnas = [b['dna'] for b in best_results]

    return dnas

if __name__ == '__main__':
    text = open('./text', 'r', encoding='utf-8', ).read()
    phrases = tokenize_text(text)

    transition_matrix, initial_state = define_parameters(phrases)

    encode_dict = generate_dna(1)[0]

    dnas = generate_dna(5)

    for i in range(10):
        text_ = encode(phrases[0], encode_dict)
        dnas = train(dnas, text_)

    print(f'Original encoding map: {encode_dict}')
    print(f'Predicted encoding map: {dnas[0]}')
