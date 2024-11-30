import csv
import random

def carregar_mapa_csv(arquivo_csv):
    """
    Carrega o mapa da cidade a partir do arquivo CSV e cria uma estrutura de matriz.
    :param arquivo_csv: Caminho para o arquivo CSV.
    :return: Dicionário com a matriz do mapa e os identificadores das regiões.
    """
    mapa = []
    regioes = []
    with open(arquivo_csv, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            mapa.append(row)
            regioes.append(row['CD_GEOCODS'])  # Mapeamos a região pelo código
    
    return mapa, regioes

def inicializar_carros(regioes, n_carros):
    """
    Associa cada carro a uma posição inicial aleatória na matriz (regiões da cidade).
    :param regioes: Lista das regiões disponíveis.
    :param n_carros: Número total de carros.
    :return: Dicionário de carros com suas posições iniciais.
    """
    carros = {}
    for i in range(n_carros):
        carros[f"Carro_{i+1}"] = random.choice(regioes)
    return carros

def mover_carros(carros, regioes, margem=1):
    """
    Move os carros aleatoriamente dentro da margem especificada.
    :param carros: Dicionário de carros e suas posições.
    :param regioes: Lista de regiões disponíveis.
    :param margem: Margem de variação para o movimento.
    :return: Dicionário atualizado com as novas posições dos carros.
    """
    regioes_num = [int(r) for r in regioes]  # Convertemos para inteiros para simular deslocamentos numéricos
    for carro, posicao in carros.items():
        posicao_num = int(posicao)
        nova_posicao = posicao_num + random.randint(-margem, margem)
        if nova_posicao in regioes_num:
            carros[carro] = str(nova_posicao)
    return carros

# Exemplo de uso
arquivo_csv = '/home/jr/ED2/Trabalho Final/bairrosGoiania.csv'  # Substitua pelo caminho correto
n_carros = 5  # Número de carros para simular
margem_variacao = 10  # Margem de movimento

# Carregar o mapa e inicializar os carros
mapa, regioes = carregar_mapa_csv(arquivo_csv)
carros = inicializar_carros(regioes, n_carros)

print("Posições iniciais dos carros:")
print(carros)

# Mover os carros
carros = mover_carros(carros, regioes, margem_variacao)

print("\nNovas posições dos carros após o movimento:")
print(carros)