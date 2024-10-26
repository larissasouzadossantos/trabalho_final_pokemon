import httpx
import pandas as pd

# Função para buscar dados de um Pokémon específico
def obter_pokemon(nome_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}"
    resposta = httpx.get(url)
    dados_pokemon = resposta.json()

    # Extrai as informações relevantes
    pokemon_info = {
        "nome": dados_pokemon['name'],
        "altura": dados_pokemon['height'],
        "peso": dados_pokemon['weight'],
        "experiencia_base": dados_pokemon['base_experience'],
        "habilidade_1": dados_pokemon['abilities'][0]['ability']['name'] if len(dados_pokemon['abilities']) > 0 else None,
        "habilidade_2": dados_pokemon['abilities'][1]['ability']['name'] if len(dados_pokemon['abilities']) > 1 else None,
    }
    return pokemon_info

# Lista de Pokémons "interessantes" para buscar
pokemons_interessantes = ["pikachu", "charmander", "squirtle"]

# Armazena os dados de cada Pokémon em uma lista
dados_pokemons = [obter_pokemon(nome) for nome in pokemons_interessantes]

# Cria um DataFrame com as informações dos três Pokémons
df = pd.DataFrame(dados_pokemons)

# Exibe o DataFrame
print(df)
