'''
    Este script Python decodifica mensagens em código Morse e as salva em um arquivo CSV com 
    um registro de data e hora. As principais funções incluem decode_morse(msg), que converte 
    código Morse em texto claro, e save_clear_msg_csv_hdr(msg), que salva a mensagem decodificada
    e o timestamp em um arquivo CSV. O arquivo é criado ou atualizado conforme necessário, garantindo
    que cada nova mensagem seja registrada adequadamente. O script é executado a partir da linha 
    de comando, permitindo que a mensagem Morse seja passada como argumento.
'''
import os
import datetime
import sys
import pandas as pd
from config import dict_morse, file_path



def decode_morse(msg):
    # Divide a mensagem em palavras usando dois espaços como delimitador
    words = msg.split("  ")
    decoded_message = []

    for word in words:
        # Divide cada palavra em letras usando um espaço simples como delimitador
        letters = word.split(" ")
        decoded_word = []
        
        for letter in letters:
            decoded_word.append(dict_morse[letter])

        # Junta as letras em uma palavra e adiciona à mensagem decodificada
        decoded_message.append("".join(decoded_word))
        
    # Junta as palavras com um espaço simples entre elas
    return " ".join(decoded_message)


def save_clear_msg_csv_hdr(msg):
    '''
    Inputs: msg (string):
    Uma string que representa uma mensagem codificada em código Morse.
    Exemplo: ".... . .-.. .-.. ---" (que corresponde a "HELLO" em texto claro).

    Outputs: Retorno
    A função não retorna nenhum valor explícito (None).
    O efeito principal da função é a criação ou atualização de um arquivo CSV onde 
    cada linha contém a mensagem decodificada e o timestamp correspondente.
    '''
    now = datetime.datetime.now()
    msg_claro = decode_morse(msg)
    df = pd.DataFrame([[msg_claro, now]], columns=["mensagem", "datetime"])
    hdr = not os.path.exists(file_path)
    df.to_csv(file_path, mode='a', index=False, header=hdr)


if __name__ == "__main__":
    save_clear_msg_csv_hdr(sys.argv[1])
