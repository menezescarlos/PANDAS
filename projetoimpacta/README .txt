=> pip freeze = mostra uma lista de tudo que eu tenho instalado de bibliotecas

=> python -m venv nomedoambiente = criação do ambiente virtual para que os pacotes instalados em outros projetos não sejam no mesmo ambiente de um novo projeto, cria-se um ambiente limpo

============================================================
ATIVANDO O AMBIENTE VIRTUAL

1. VAI ATÉ O DIRETORIO CRIADO SEGUINDO O CAMINHO

  => projetoimpacta\Scripts\activate

 CASO TENHA PROBLEMAS PARA ATIVAÇÃO DEVE RODAR OS COMANDOS     NO POWER SHELL

1. Isso mostrará a política de execução atual. Provavelmente estará configurada como Restricted.
=> Get-ExecutionPolicy

2. Para permitir a execução de scripts, você pode definir a política como RemoteSigned (scripts baixados da internet devem ser assinados por um editor confiável) ou Unrestricted (sem restrições para execução de scripts):
=> Set-ExecutionPolicy RemoteSigned

Ou, se preferir permitir todos os scripts, use
=> Set-ExecutionPolicy Unrestricted

3. Agora, tente executar novamente o comando:
=> projetoimpacta\Scripts\activate

PARA DESATIVAR ABIENTE VIRTUAL É SO USAR O COMANDO
=> desactivate

===========================================================
PARA EXECUTAR UM ARQUIVO PYTHON

=> python .\nomedoarquivo.py

==========================================================

PARA INSTALAR NOVOS PACOTES POIS NÃO POSSUI NENHUM PACOTE NO AMBIENTE VIRTUAL

=> pip install pandas

===========================================================

VARIAVEL DE AMBINETE

1. Para criar uma variável de ambiente crie um arquivo
=> .env

==========================================================

LINK PARA A CRIAÇÃO ALTOMATICA DO GITIGNORE
=> https://www.toptal.com/developers/gitignore

===========================================================

BIBLIOTECAS PARA IMPORTAR VARIÁVEIS DE AMBIENTE

1. PARA INSTALAR O DOTENV
=> pip install python-dotenv

2.PARA USAR O PACOTE NO PROJETO, A FIM DE UTILIZAR AS VARIÁVEIS DE AMBIENTE.
=> from dotenv import load_dotenv

load_dotenv()
file_path = os.getenv("file_path")

=============================================================

PARA ANALISAR O MEU CODIGO
=> pylint nomedoarquivo.py

CASO O PYLINT NÃO ESTEJA INTALADO UTILIZES OS COMANDO

PARA CONFIRMAR SE ESTÁ INSTALADO
=>pip list | findstr pylint

PARA INSTALAR O PYLINT
=>pip install pylint

============================================================

PARA RODAR O PROGRAMA COM DUAS PALAVRAS COM 2 ESPAÇOS

python .\desafiotrabalho.py '-.-. .- .-.  --- .-.. .. -. .-'






