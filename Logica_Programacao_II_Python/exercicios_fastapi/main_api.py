import os
import time
import json
import itertools
from typing import Tuple
from fastapi import Body, Request, FastAPI

app = FastAPI()

def get_json_data(filename: str) -> dict:

    with open(filename,'r') as f:
        data = json.load(f)
        
    return data    

@app.get("/requisicao/{file_code}")
def get_json_content(file_code: str) -> dict:
    
    root = os.getcwd()
    
    data = get_json_data(os.path.join(root,file_code+'.json'))    
    
    return data
    
@app.post("/json_post/{file_code}")
def post_json_content(file_code: str, content: dict) -> dict:
    
    root = os.getcwd()
    
    with open(os.path.join(root,file_code+'.json'),'w') as f:
        json.dump(content,f)    
    
    return {"Message": "JSON criado"}
    
@app.get("/total")
def get_total():
    
    root = os.getcwd()
    
    inicio = time.time()
    
    files       = [os.path.join(root,x) for x in os.listdir(root) if x.endswith('.json')]
    valor_total = 0
    for f in files:
        data         = get_json_data(f)
        try:
            valor_total += float(data["venda"]["valorFinal"])
        except:
            pass       
    
    fim    = time.time()       
    tempo  = fim - inicio
    
    return valor_total, tempo
    
@app.get("/total_loja")
def get_total_loja():
    
    root   = os.getcwd()
    
    inicio = time.time()
    
    files             = [os.path.join(root,x) for x in os.listdir(root) if x.endswith('.json')]
    
    somatorio_loja = {}
    
    for f in files:
        data  = get_json_data(f)
        try:
            loja  = data["loja"]["codigo"]
            valor = data["venda"]["valorFinal"]
        
            if loja in somatorio_loja.keys():
                somatorio_loja[loja] = round(somatorio_loja[loja] + valor,2)
            else:
                somatorio_loja[loja] = valor
        except:
            pass        
    
    fim    = time.time()       
    tempo  = fim - inicio
    
    return somatorio_loja, tempo   
    
@app.post("/atualizar_loja/{loja}/{valor_novo}")
def atualizar_loja(loja:str, valor_novo: float) -> dict:
    
    root   = os.getcwd()
    files             = [os.path.join(root,x) for x in os.listdir(root) if x.endswith('.json')]
    for f in files:
        data = get_json_data(f)
        try:
            cod_loja = data["loja"]["codigo"]
            if cod_loja == loja:
                data["venda"]["valorFinal"] = float(valor_novo)
                
                with open(f,'w') as file_path:
                    json.dump(data,file_path,indent=2, ensure_ascii=False)
        except:
            pass            
                    
    return {"Sucesso": "Valores atualizados"}                         
