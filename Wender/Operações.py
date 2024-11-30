import json

# Classe TabelaHash com tratamento de colisões por encadeamento separado
class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]  # Lista de listas para encadeamento

    def funcao_hash(self, chave):
        """
        Função hash que retorna o índice onde o item será armazenado.
        Usamos o hash built-in do Python e garantimos que o índice caia dentro
        do tamanho da tabela.
        """
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        """
        Insere um item na tabela hash. Em caso de colisão, o item é adicionado à lista
        de itens na mesma posição da tabela.
        """
        indice = self.funcao_hash(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:
                item[1] = valor  # Atualiza o valor se a chave já existir
                return
        self.tabela[indice].append([chave, valor])  # Adiciona a chave e valor

    def buscar(self, chave):
        """
        Busca por um item na tabela hash. Retorna o valor associado à chave se encontrar.
        """
        indice = self.funcao_hash(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:
                return item[1]
        print("Placa não encontrada")
        return None  # Retorna None se a chave não for encontrada

# Função para carregar o dataset JSON do Google Drive ou qualquer caminho do Colab
def carregar_dataset_json(caminho_arquivo):
    """
    Carrega o arquivo JSON a partir do caminho fornecido e retorna os dados.
    """
    with open(caminho_arquivo, 'r') as file:
        dataset = json.load(file)
    return dataset

# Função de menu interativo
def menu():
    # Caminho para o arquivo JSON
    caminho_arquivo_json = '/home/jr/Trafego-Urbano/dataset_versao1-carros/dataset'  # Substitua com o caminho correto

    # Carregar os dados do arquivo JSON
    dataset = carregar_dataset_json(caminho_arquivo_json)

    # Criar a instância da Tabela Hash
    tamanho_tabela = 50
    tabela_hash = TabelaHash(tamanho_tabela)

    # Preencher a Tabela Hash com os dados do JSON
    for item in dataset:
        chave = item["placa"]  # Usamos a placa como chave
        valor = item  # O valor é o registro completo
        tabela_hash.inserir(chave, valor)

    while True:
        print("\nMenu:")
        print("1. Buscar um veículo pela placa")
        print("2. Inserir um novo registro (placa e dados)")
        print("3. Exibir todos os registros na tabela hash")
        print("4. Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, digite um número válido!")
            continue

        if opcao == 1:
            placa_teste = input("Digite a placa do veículo: ")
            resultado_busca = tabela_hash.buscar(placa_teste)
            if resultado_busca:
                print(f"Resultado da busca para a placa {placa_teste}: {resultado_busca}")
            else:
                print(f"Placa {placa_teste} não encontrada.")

        elif opcao == 2:
            chave = input("Digite a placa do veículo: ")
            dados = input("Digite os dados do veículo (em formato JSON): ")
            try:
                valor = json.loads(dados)
                tabela_hash.inserir(chave, valor)
                print("Registro inserido com sucesso!")
            except json.JSONDecodeError:
                print("Os dados do veículo devem estar em formato JSON válido!")

        elif opcao == 3:
            print("\nTabela Hash:")
            for i, bucket in enumerate(tabela_hash.tabela):
                print(f"Bucket {i}: {bucket}")

        elif opcao == 4:
            print("Saindo...")
            break

        else:
            print("Opção inválida! Por favor, tente novamente.")

# Iniciar o menu
if __name__ == "__main__":
    menu()