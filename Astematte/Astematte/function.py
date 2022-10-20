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
    result_int = ''.join(random.choice(l) for _ in range(n))
    #result_int = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    return result_int