"""
Funzioni generali da settare durante la creazione della Web App
Inserire qui cosa c'è specificato in ogni funzione in generale:
- get_random_string_upp_dig(n) --> Genera una stringa casuale con n caratteri tra MAIUSCOLE e NUMERI senza i seguenti: ['I', '1', '0', 'O']

## Data aggiornamento 17/10/2022 ##
## Autore: Giuseppe Ambrosio ##

"""

import random

def get_random_string_upp_dig(n):
    l = ['2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','W','X','V','Z']
    return ''.join(random.choice(l) for _ in range(n))

""" Funzione che verifica se un valore esiste già """
"""
def test():
    a = 'AA'
    lettere = ['A', 'B']
    testing = ''.join(random.choice(lettere) for _ in range(2))
    print(a)
    print(testing)
    print('--------')
    while a == testing:
        testing = ''.join(random.choice(lettere) for _ in range(2))
        print(testing)
"""