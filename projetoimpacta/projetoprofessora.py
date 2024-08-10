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
#from dotenv import load_dotenv
from config import dict_morse, file_path

#load_dotenv()
#file_path = os.getenv("file_path")
#msg = '-.-. .- .-.  --- .-.. .. -. .-'


def decode_morse(msg):
    '''
    Inputs: msg (string):
    Uma string que representa uma mensagem codificada em código Morse.
    As letras e símbolos em código Morse são separados por espaços simples (" ").
    Exemplo: ".... . .-.. .-.. ---" (que corresponde a "HELLO" em texto claro).

    Outputs: Retorno (string)
    Uma string que representa a mensagem decodificada em texto claro (alfabeto comum).
    Exemplo: para o input ".... . .-.. .-.. ---", a função retornaria "HELLO".
    '''

    msg_lst = msg.split(" ")
    msg_claro = [] 
    for letter in msg_lst :
        msg_claro.append(dict_morse[letter])
    return "".join(msg_claro)



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

    #print(file_path)