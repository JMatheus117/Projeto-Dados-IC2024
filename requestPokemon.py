# Projeto de Dados IC2024 - Request API Pokemon

import requests  # importado a biblioteca para requisição de API
import pandas as pd  # importado a biblioteca para manipulação e análise de dados gerar CSV

def consul_poke(Poke_id):  # função para chamar a API com if para testar a resposta
    url = f'https://pokeapi.co/api/v2/pokemon/{Poke_id}'
    status = requests.get(url)
    if status.status_code == 200:  # primeiro if testa API para id e nome
        info = status.json()
        name = info['name']
        url_local = info['location_area_encounters']  # solicitar url de local
        statusLocal = requests.get(url_local)          
        if statusLocal.status_code == 200:
            local_info = statusLocal.json()
            if local_info:
                local = [busca['location_area']['name'] for busca in local_info]
                return {"Nome": name, "ID": Poke_id, "Localização": ", ".join(local)}
            else:
                return {"Nome": name, "ID": Poke_id, "Localização": "Não encontrado"}
    return None

pokemon_list = []
# Definindo o intervalo de Pokémons (pode ser ajustado conforme necessário)
for i in range(150, 152): 
    pokedex = consul_poke(i)
    if pokedex:
        pokemon_list.append(pokedex)
        print(pokedex)

# CRIANDO A LISTA E COLUNA
colunas = ['Nome', 'ID', 'Localização']
df = pd.DataFrame(pokemon_list)

# SALVANDO E CONVERTENDO EM CSV
df.to_csv('pokemon_data.csv', encoding='utf-8', index=False)

print("Dados dos Pokémons capturados com sucesso!")
