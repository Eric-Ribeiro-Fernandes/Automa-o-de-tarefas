import os
import pandas as pd 
import numpy as np 
import re 
import PyPDF2 as pdf 

def module_init():
    print("\n")
    print("Seu diretório atual é: " + str(os.getcwd()))
    try:
        print("\n")
        r =input("Deseja mudar de diretório? [y/n]")
        if r =='y':
            return select_directory()
        elif r =='n':
            global directory
            directory = str(os.getcwd())
            return list_directorys()
        else:
            print("\n")
            print("Comando inválido")
            return module_init()
    except KeyboardInterrupt:
        print("\n")
        r =input("Deseja voltar ao menu inicial? [y/n]")
        if r == 'y':
            import teste_de_input
            teste_de_input.initialization()
        else:
            return module_init()
def select_directory():
    try:
        global directory
        directory = input("Informe o diretório em que o arquivo se encontra:")
        os.chdir(directory)
        print("\n")
        print("Done")
        list_directorys()
    except KeyboardInterrupt:
        r =input("Deseja voltar ao menu inicial? [y/n]")
        if r == 'y':
            import teste_de_input
            teste_de_input.initialization()
        else:
            return select_directory()
def list_directorys():
    try:
        arquivos = os.listdir(directory)
        global df_files
        df_files = pd.DataFrame(arquivos, columns=['Arquivos'])
        print("\n")
        print(df_files)
        print("\n")
        File()
    except KeyboardInterrupt:
        print("\n")
        r =input("Deseja voltar ao menu inicial? [y/n]")
        if r == 'y':
            import teste_de_input
            teste_de_input.initialization()
        else:
            return list_directorys()
def File():
    File = 0
    while File < len(df_files):
        try:
            File = df_files.iloc[int(input("Insira o índice do arquivo:"))].to_string()
            global File_split
            File_split = File.rsplit("Arquivos    ")[1]
            open_pdf()
        except ValueError:
            print("\n")
            print("Insira um número inteiro")
        except IndexError:
            print("\n")
            print("Esse índice não existe")
        except KeyboardInterrupt:
            print("\n")
            r =input("Deseja voltar ao menu inicial? [y/n]")
            if r == 'y':
                import teste_de_input
                teste_de_input.initialization()
            else:
                return open_pdf()
    
def open_pdf():
    pdf_file = open(directory +"\\"+File_split, 'rb')
    global pdf_Reader
    pdf_Reader = pdf.PdfFileReader(pdf_file)
    print("\n")
    print("Arquivo '"+ str(File_split)+"' carregado com sucesso")
    print("\n")
    return menu_functions()

def menu_functions():
    df_menu = pd.DataFrame(data=['Extrair texto','Extrair tabelas'],columns=['Funções'])
    df_menu.index = df_menu.index +1
    print("\n")
    print(df_menu)
    print("\n")
    r = input("Escolha a função que deseja aplicar ao arquivo: ")
    if r == '1':
        return func_extrair_texto()
    elif r =='2':
        return func_extrair_tabelas()
    else:
        print("\n")
        print("Comando inválido")
        
        return menu_functions()

def func_extrair_texto():
    df_extrair = pd.DataFrame(data=['Extrair página','Extrair documento inteiro'],columns=['Funções'])
    df_extrair.index = df_extrair.index +1
    print("\n")
    print(df_extrair)
    print("\n")
    r = input("Escolha a função que deseja aplicar ao arquivo: ")
    if r == '1':
        num = pdf_Reader.numPages + 1
        print("O arquivo possui " + str(num) +" páginas")
        print("\n")
        pag = int(input("Selecione a página que deseja extrair: ")) -1
        pageObj = pdf_Reader.getPage(pag)
        content = pageObj.extractText()
        output =open('C:/Users/ADM/Desktop/Temporários/Output_PDF_module/PDF_txt.txt','w',encoding='UTF-8')
        output.write(content)
        output.close()




def func_extrair_tabelas():
    print("")

