import xmltodict
import os
import json
import pandas as pd

def pegar_infos(nome_arquivo, valores):
    #print(f"Pegou as informações {nome_arquivo}")
    with open(f'nfs/{nome_arquivo}', "rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)
        
    
        if "NFe" in dic_arquivo:
            infos_nf = dic_arquivo["NFe"]["infNFe"]
        else:
            infos_nf = dic_arquivo["nfeProc"]["NFe"]["infNFe"]

        numero_nota = infos_nf["@Id"]
        empresa = infos_nf["emit"]["xNome"]
        cliente = infos_nf["dest"]["xNome"]
        endereco = infos_nf["dest"] ["enderDest"]
        if "vol" in infos_nf["transp"]:
            peso = infos_nf["transp"]["vol"]["pesoB"]
        else: 
            peso = "Não informado"
        valores.append([numero_nota, empresa, cliente, endereco, peso])


lista_arquivos = os.listdir("nfs")

colunas = ["numero", "empresa","cliente", "endereco","peso"]
valores = []

for arquivo in lista_arquivos:
    pegar_infos(arquivo, valores)

tabela = pd.DataFrame(columns=colunas, data=valores)
print(tabela)
tabela.to_excel("NotasFiscais.xlsx", index=False)