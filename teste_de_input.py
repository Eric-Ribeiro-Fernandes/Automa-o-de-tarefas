# Verificação do usuário
""" from getpass import getpass
tentativas = 3
Senha = ""
while tentativas != 0:
    print("Você possui " + str(tentativas) + " tentativas")
    Senha = getpass("Senha:")
    if Senha == "entropia":
        print("Acesso permitido Eric musculoso")
        break
    elif tentativas == 1:
        print("Não consegue né Moisés")
        exit()
    else:
        print("Acesso negado")
    tentativas -= 1 """

# Menu inicial
import pandas as pd 
import os
df_module = pd.DataFrame(data=['Arquivos .txt','Arquivos Excel','Arquivos em PDF'],columns=['Module'])
df_module.index = df_module.index +1

def initialization():
    print(df_module)
    global module
    module = input('>:')
    if module == '1':
        return module_txt()
    elif module =='2':
        return module_excel()
    elif module == '3':
        return module_pdf()
    else:
        print("MÓDULO INEXISTENTE")
        return initialization()

# Módulo .txt
def module_txt():
    print("Módulo .txt selecionado")
    import module_txt as txt
    # Execução de tarefas
    txt.module_init()
    
# Módulo Excel
def module_excel():
    print("Módulo excel selecionado")
# Módulo PDF
def module_pdf():
    print("Módulo PDF selecionado")
    import module_PDF as PDF
    PDF.module_init()
# Escolhendo o módulo
print("Bem-vindo ao primeiro protótipo de interação entre homem e máquina\nSelecione o módulo que deseja")
initialization()

# Execuções

