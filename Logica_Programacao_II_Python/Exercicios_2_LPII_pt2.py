import json
import base64, os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

'''
3. Crie um dicionário com informações pessoais de usuários, como nome, endereço, telefone etc. Converta o dicionário em uma string JSON e criptografe-a usando uma técnica de criptografia 
simétrica. Escreva a string criptografada em um arquivo TXT. Implemente uma função que lê o arquivo TXT, descriptografa a string JSON e reconstrói o dicionário original.
'''

def criptografa(dicionario,nome_arquivo,key):

    string_json = json.dumps(dicionario)
    data = string_json.encode('ascii')
    
    cipher = AES.new(key, AES.MODE_EAX) 
    ciphertext, tag = cipher.encrypt_and_digest(data)
    
    f = open(nome_arquivo,'wb')
    [f.write(x) for x in (cipher.nonce, tag, ciphertext)]
    f.close()
    
def descriptografa(nome_arquivo, key):

    f = open(nome_arquivo,'rb')
    nonce, tag, ciphertext = [f.read(x) for x in (16,16,-1)]
    f.close()
    
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext,tag)
    
    string_json = data.decode('ascii')
    dicionario = json.loads(string_json)   
    
    return dicionario 
    
def funcao_cripto(texto):

    texto_criptografado = ""
    for char in texto:
        char_cripto = chr(ord(char) + 3)
        texto_criptografado += char_cripto
        
    return texto_criptografado
    
def funcao_decripto(texto):

    texto_descriptografado = ""
    for char in texto:
        char_decripto = chr(ord(char) - 3)
        texto_descriptografado += char_decripto
        
    return texto_descriptografado
    
def criptografa_v2(dicionario,nome_arquivo):

    texto = json.dumps(dicionario)
    criptografado = funcao_cripto(texto)
    f = open(nome_arquivo,'w',encoding='utf-8')
    f.write(criptografado)
    f.close()
    
def descriptografa_v2(nome_arquivo):

    f = open(nome_arquivo,'r',encoding='utf-8')
    criptografado = f.read()
    f.close()
    texto = funcao_decripto(criptografado)
    dicionario = json.loads(texto)
    
    return dicionario                          
    
def main():
    
    infos_usuarios = {
         1: {
              "nome": "Fernanda",
              "endereco": "Cacapava",
              "telefone": "(12)9999-9999"
            },
         2: {
              "nome": "João",
              "endereco": "Jacarei",
              "telefone": "(12)9998-9998"
            },
         3: {
              "nome": "Maria",
              "endereco": "Sao Jose dos Campos",
              "telefone": "(12)9797-9797"
            } 
    }
    
    nome_arquivo = 'criptografado.bin'
    key          = get_random_bytes(16)
    criptografa(infos_usuarios,nome_arquivo,key)  
    
    dicionario   = descriptografa(nome_arquivo,key)
    print(type(dicionario))
    print(dicionario)
    
    nome_arquivo = 'criptografado_v2.txt'
    criptografa_v2(infos_usuarios,nome_arquivo)  
    
    dicionario   = descriptografa_v2(nome_arquivo)
    print(type(dicionario))
    print(dicionario)

if __name__=="__main__":

    main()
