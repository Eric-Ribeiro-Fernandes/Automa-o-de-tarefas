
# Bibliotecas
import pandas as pd 
import os
import module_txt as txt
import module_word as word

# Verificação do usuário
# def log_in():
#     from getpass import getpass
#     tentativas = 3
#     Senha = ""
#     while tentativas != 0:
#         print("Você possui", tentativas, "tentativas")
#         Senha = getpass("Senha:")
#         if Senha == "entropia":
#             print("Acesso permitido Eric musculoso")
#             print("\nBem-vindo ao primeiro protótipo de interação entre homem e máquina\nSelecione o módulo que deseja\n")
#             initialization()
#             break
#         elif tentativas == 1:
#             print("Não consegue né Moisés")
#             exit()
#         else:
#             print("Acesso negado")
#         tentativas -= 1 

# Menu inicial
# Escolhendo o módulo
def initialization():
    df_module = pd.DataFrame(data=['Arquivos .txt','Arquivos Excel','Scrapping Word'],columns=['Module'])
    df_module.index = df_module.index +1
    print(df_module)
    global module
    module = None
    while module != ('1' or '2' or '3'):
        module = input('\n>:')
        if module == '1':
            print("\nMódulo .txt selecionado\n")
            return txt.module_init()
        elif module =='2':
            print("\nMódulo excel selecionado")
            pass
        elif module == '3':
            print("\nMódulo Scrapping Word selecionado")
            return word.module_init()
        else:
            print("\nMÓDULO INEXISTENTE")


# Execuções
initialization()

