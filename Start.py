
# Bibliotecas
import pandas as pd 
import os

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
def initialization():
    df_module = pd.DataFrame(data=['Arquivos .txt','Arquivos Excel','Scrapping Word'],columns=['Module'])
    df_module.index = df_module.index +1
    print(df_module)
    global module
    module = input('\n>:')
    if module == '1':
        return module_txt()
    elif module =='2':
        return module_excel()
    elif module == '3':
        return Scrapping_word()
    else:
        print("\nMÓDULO INEXISTENTE")
        return initialization()

# Escolhendo o módulo

# Módulo .txt
def module_txt():
    print("\nMódulo .txt selecionado\n")
    import module_txt as txt
    # Execução de tarefas
    txt.module_init()


# Módulo Excel
def module_excel():
    print("\nMódulo excel selecionado")

# Módulo PDF
def Scrapping_word():
    print("\nMódulo Scrapping Word selecionado")
    import module_word as word
    word.initialization()


# Execuções
initialization()

