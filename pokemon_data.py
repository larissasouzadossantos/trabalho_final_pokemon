# Importa as bibliotecas httpx (para fazer requisições HTTP) e pandas (para trabalhar com tabelas de dados)
import httpx
import pandas as pd

# Função que exibe uma mensagem de alerta quando ocorre um erro
def alerta(mensagem):
    print(f"Alerta: {mensagem}")

# Função para obter dados de um Pokémon usando a PokeAPI
def obter_pokemon(nome_pokemon):
    try:
        # Constrói a URL com o nome do Pokémon
        url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}"
        # Faz a requisição à API
        resposta = httpx.get(url)
        # Verifica se houve erro na requisição
        resposta.raise_for_status()
        # Extrai os dados em formato JSON
        dados_pokemon = resposta.json()

        # Organiza os dados em um dicionário com as informações do Pokémon
        pokemon = {
            "nome": dados_pokemon['name'],
            "tipo_1": dados_pokemon['types'][0]['type']['name'],
            "tipo_2": dados_pokemon['types'][1]['type']['name'] if len(dados_pokemon['types']) > 1 else None,
            "hp": dados_pokemon['stats'][0]['base_stat'],
            "ataque": dados_pokemon['stats'][1]['base_stat'],
            "defesa": dados_pokemon['stats'][2]['base_stat'],
            "ataque_especial": dados_pokemon['stats'][3]['base_stat'],
            "defesa_especial": dados_pokemon['stats'][4]['base_stat'],
            "velocidade": dados_pokemon['stats'][5]['base_stat'],
        }
        return pokemon
    except Exception as e:
        alerta(f"Erro ao obter dados do Pokémon: {e}")
        return None

# Lista com os nomes dos Pokémons que você quer buscar na API
pokemons_para_buscar = ["pikachu", "charmander", "squirtle"]

# Lista vazia para armazenar os dados dos Pokémons
dados_pokemons = []

# Para cada nome de Pokémon na lista, chama a função obter_pokemon e salva os dados
for nome_pokemon in pokemons_para_buscar:
    pokemon = obter_pokemon(nome_pokemon)
    if pokemon:
        dados_pokemons.append(pokemon)

# Cria uma tabela de dados com pandas usando a lista de Pokémons
df = pd.DataFrame(dados_pokemons)

# Exibe a tabela no console
print(df)

