import json
import requests

url = 'http://localhost:8000/json_post/teste_dicionario'

dicionario = {
   "nome": "Joao",
   "sobrenome": "Silva",
   "idade": 45
}

response = requests.request("POST", url, json=dicionario)
print(response.json())


#se for @app.post na main_api.py
#se for @app.get, pegar no localhost:8000/total
#url = 'http://localhost:8000/total'
#response = requests.request("POST", url)
#print(response.json())

url = 'http://localhost:8000/atualizar_loja/L002/80.50'
response = requests.request("POST", url)
print(response.json())
