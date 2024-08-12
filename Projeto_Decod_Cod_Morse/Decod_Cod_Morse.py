import os
import datetime
import pandas as pd
from config import dict_morse, file_path



#dict_morse = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F","--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L","--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R","...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X","-.--": "Y", "--..": "Z", "-----": 0, ".----": 1, "..---": 2, "...--": 3,"....-": 4, ".....": 5, "-....": 6, "--...": 7, "---..": 8, "----.": 9}
#file_path = 'msg_traduzida.txt'

msg = str(input('Digite o código morse: '))


def decodificar_msg(msg, dict_morse):
    mensagem_decodificada = []
    sep_palavra = msg.split('  ')
    for palavra in sep_palavra:
        palavra_decodificada = []
        letras = palavra.split(' ')
        for letra in letras:
            if letra in dict_morse:
                palavra_decodificada.append(dict_morse[letra])
            else:
                palavra_decodificada.append('?')  # Para tratar caracteres não reconhecidos
        mensagem_decodificada.append(''.join(str(char) for char in palavra_decodificada)) # Para transformar tudo em string
    return ' '.join(mensagem_decodificada)


def save_clear_msg_csv_hdr(file_path, msg, dict_morse):
    now = datetime.datetime.now()
    msg_claro = decodificar_msg(msg, dict_morse)
    df = pd.DataFrame([[msg_claro, now]], columns = ['mensagem', 'datetime'])
    hdr = not os.path.exists(file_path)
    df.to_csv(file_path, mode = 'a', index = False, header = hdr)


if __name__ == "__main__":
    save_clear_msg_csv_hdr(file_path, msg, dict_morse)