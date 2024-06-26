from permutation import Permutation, create_identity, create_random_permutation
import numpy as np

#chars = 'abcdefghijklmnopqrstuvwxyz0123456789 ,.?!:;'
chars='aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż ,.?!:;'
def encode_text(text: str, permutation: Permutation) -> str:
    out = list(text)
    for i in range(len(out)):
        out[i] = chars[permutation(index(text[i]))]
    return "".join(out)

def index(letter: str) -> int:
    return chars.find(letter.lower())

def adjecency_matrix(text: str) -> np.ndarray:
    matrix = np.zeros((len(chars), len(chars)), dtype = np.float32)
    for i in range(len(text) - 1):
        matrix[index(text[i])][index(text[i + 1])] += 1
    for i in range(len(chars)):
        S = sum(matrix[i])
        if S > 0:
            matrix[i] += 1
            matrix[i] /= S
    return np.log(matrix)

def distribution_vector(text: str) -> np.ndarray:
    vect = np.array([text.count(letter) for letter in chars], dtype=np.float32)
    vect += 1
    vect /= len(text)
    return np.log(vect)
    