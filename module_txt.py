# Bibliotecas
import os
import pandas as pd 
import re
import numpy as np 

# Informando o arquivo txt
def module_init():
    os.chdir("C:/Users/ADM/Desktop/Temporários/Rats") # rats significa a pasta aonde estão os arquivos a serem analizados
    print("Seu diretório atual é: C:/Users/ADM/Desktop/Temporários/Rats" )
    r =input("Deseja mudar de diretório? [y/n]")
    try:
        
        if r =='y':
            return select_directory()
        elif r =='n':
            global directory
            directory = str(os.getcwd())
            return list_directorys()
        else:
            print("Comando inválido")
            return module_init()
    except KeyboardInterrupt:
        r =input("Deseja voltar ao menu inicial? [y/n]")
        if r == 'y':
            import Start
            Start.initialization()
        else:
            return module_init()

# Função para trocar o diretório
def select_directory():
    try:
        global directory
        directory = input("Informe o diretório em que o arquivo se encontra:")
        os.chdir(directory)
        print("Done")
        list_directorys()
    except KeyboardInterrupt:
        r =input("Deseja voltar ao menu inicial? [y/n]")
        if r == 'y':
            import Start
            Start.initialization()
        else:
            return select_directory()

# Função que lista os arquivos do diretório com indice
def list_directorys():
    try:
        arquivos = os.listdir(directory)
        global df_files
        df_files = pd.DataFrame(arquivos, columns=['Arquivos'])
        print(df_files)
        File()
    except KeyboardInterrupt:
        r =input("Deseja voltar ao menu inicial? [y/n]")
        if r == 'y':
            import Start
            Start.initialization()
        else:
            return list_directorys()

# Carrega o arquivo txt
def File():
    try:
        File = df_files.iloc[int(input("Insira o índice do arquivo:"))].to_string()
        global File_split
        File_split = File.rsplit("Arquivos    ")[1]
        open_txt()
    except ValueError:
        print("Insira um número inteiro")
    except IndexError:
        print("Esse índice não existe")
    except KeyboardInterrupt:
        r =input("Deseja voltar ao menu inicial? [y/n]")
        if r == 'y':
            import Start
            Start.initialization()
        else:
            return open_txt()
def open_txt():
    text_file = open(directory +"\\"+File_split, encoding="UTF-8")
    print("Arquivo '"+ str(File_split)+"' carregado com sucesso")
    global text 
    text = text_file.read()
    text_file = open(directory +"\\"+File_split, encoding="UTF-8")
    global t_lines
    t_lines = text_file.readlines()
    text_file.close()

    return menu_functions()

# Escolha de função a ser implementada no arquivo selecionado
def menu_functions():
    df_menu = pd.DataFrame(data=['Procurar telefones','Procurar emails'],columns=['Funções'])
    df_menu.index = df_menu.index +1
    print(df_menu)
    r = input("Escolha a função que deseja aplicar ao arquivo: ")
    if r == '1':
        return func_telefones()
    elif r =='2':
        return func_emails()
    else:
        print("Comando inválido")
        return menu_functions()

# Busca telefone por REGEX
def func_telefones():
    telefones = re.findall(r'[\b(][0-9]{2}[)] ?9?\d{4}\D?\d{4}\b|\b[0-9]{2} ?9?\d{4}\D?\d{4}\b|\b9?\d{4}\D?\d{4}\b',text)
    linha = []
    for t in t_lines:
        r =re.findall(r'[\b(][0-9]{2}[)] ?9?\d{4}\D?\d{4}\b|\b[0-9]{2} ?9?\d{4}\D?\d{4}\b|\b9?\d{4}\D?\d{4}\b',t)
        if len(r) == 1:
            linha.append(t_lines.index(t)+1)
        elif len(r) > 1:
            i = len(r)
            while i > 0:
                linha.append(t_lines.index(t)+1)
                i-=1

    t_position = []
    tel_no_DDD = re.findall(r'\b[0-9]{2} ?9?\d{4}\D?\d{4}\b|\b9?\d{4}\D?\d{4}\b',text)
    for t in tel_no_DDD:
        r = re.search(t,text)
        t_position.append(r.start())    
    np_telefones = np.array(telefones)
    np_linhas = np.array(linha)
    np_position = np.array(t_position)

    df_telefones = pd.DataFrame()
    df_telefones['Telefone encontrado'] =np_telefones
    df_telefones['Linha no documento'] = np_linhas
    df_telefones['Posição inicial cursor']=np_position
    print(df_telefones)

    s = ""
    while s != 'y' or s != 'n':
        
        s = input('Deseja salvar Output? [y/n]')
        
        if s == 'y':
            out_txt = str(df_telefones)
            output =open("C:/Users/ADM/Desktop/Temporários/Output_txt_module/Output.txt",'w',encoding='UTF-8')
            output.write(out_txt)
            output.close()
            df_telefones.to_csv('C:/Users/ADM/Desktop/Temporários/Output_txt_module/Output.csv',encoding="UTF-8")
            df_telefones.to_excel('C:/Users/ADM/Desktop/Temporários/Output_txt_module/Output.xlsx')
            return menu_functions()
        elif s =='n':
            return menu_functions()
        else:
            print("Comando inválido")

# Busca e-mails por REGEX   
def func_emails():
    emails = re.findall(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.com\.?b?r?\b',text)
    linha = []
    for t in t_lines:
        r =re.findall(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.com\.?b?r?\b',t)
        if len(r) == 1:
            linha.append(t_lines.index(t)+1)
        elif len(r) > 1:
            i = len(r)
            while i > 0:
                linha.append(t_lines.index(t)+1)
                i-=1

    t_position = []
    tel_no_DDD = re.findall(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.com\.?b?r?\b',text)
    for t in tel_no_DDD:
        r = re.search(t,text)
        t_position.append(r.start())    
    np_emails = np.array(emails)
    np_linhas = np.array(linha)
    np_position = np.array(t_position)

    df_emails = pd.DataFrame()
    df_emails['Email encontrado'] =np_emails
    df_emails['Linha no documento'] = np_linhas
    df_emails['Posição inicial cursor']=np_position
    print(df_emails)

    s = ""
    while s != 'y' or s != 'n': 
        s = input('Deseja salvar Output? [y/n]')
        if s == 'y':
            out_txt = str(df_emails)
            output =open("C:/Users/ADM/Desktop/Temporários/Output_txt_module/Output.txt",'w',encoding='UTF-8')
            output.write(out_txt)
            output.close()
            df_emails.to_csv('C:/Users/ADM/Desktop/Temporários/Output_txt_module/Output.csv',encoding="UTF-8")
            df_emails.to_excel('C:/Users/ADM/Desktop/Temporários/Output_txt_module/Output.xlsx')
            return menu_functions()
        elif s =='n':
            return menu_functions()
        else:
            print("Comando inválido")
        
