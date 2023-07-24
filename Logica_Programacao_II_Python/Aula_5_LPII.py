### Aula 5 - Arquivos

import json

def remover_valor(nome_arquivo,valor):
    with open(nome_arquivo,'r') as arquivo:
        linhas = []
        for linha in arquivo:
            if valor != linha.split('\n')[0]:
                linhas.append(linha)
    with open(nome_arquivo,'w') as arquivo:
        for linha in linhas:
            arquivo.write(linha)
            
def remover_valor_v2(nome_arquivo,valor):
    with open(nome_arquivo,'r') as arquivo:
        linhas = arquivo.readlines()
    
    with open(nome_arquivo,'w') as arquivo:
        for linha in linhas:
            if valor != linha.split('\n')[0]:
                arquivo.write(linha)            
            
def substituir_valor(nome_arquivo,valor,substituto):
    with open(nome_arquivo,'r') as arquivo:
        linhas = arquivo.readlines()
    
    with open(nome_arquivo,'w') as arquivo:
        for linha in linhas:
            if valor == linha.split('\n')[0]:
                new_linha = linha.replace(valor,substituto) 
                arquivo.write(new_linha)
            else:
                arquivo.write(linha) 
                
def substituir_valor_json(nome_arquivo,chave,valor,substituto):

    with open(nome_arquivo,'r') as arquivo:
        data = json.load(arquivo)
    
    if chave in data.keys():
        if data[chave] == valor:
            data[chave] = substituto
        else:
            print(f'A chave existe mas não possui o valor {valor}')
    else:
        print(f'Não existe a chave {chave}')            
    
    with open(nome_arquivo,'w') as arquivo:
        json.dump(data,arquivo)                                  
            
remover_valor_v2('arquivo.txt','6')                         
substituir_valor('arquivo.txt','1','20')

dicionario = {
   "nome": "Joao",
   "sobrenome": "Silva",
   "idade": 45
}

with open('dicionario.json','w') as arquivo:
    json.dump(dicionario,arquivo)
    
substituir_valor_json('dicionario.json','nome','Joao','Maria') #substitui Joao por Maria
substituir_valor_json('dicionario.json','nome','Joao','Maria') #não existe mais João como valor da chave nome, então printa A chave existe mas não possui o valor Joao
substituir_valor_json('dicionario.json','rg',473333,52222) #não existe chave rg
