# ⚠️⚠️⚠️⚠️⚠️INSTRUÇÕES PARA INICIAR ESSE APLICATIVO⚠️⚠️⚠️⚠️
# INSTALAR A BIBLIOTECA MATPLOTLIB
pip install matplotlib


# ROTEIRO DE AULA PRÁTICA
# NOME DA DISCIPLINA: LINGUAGEM DE PROGRAMAÇÃO
# Unidade: 2 – Explorando Recursos do Python
# Aula: 4 – Bibliotecas e Módulos Em Python
# Author: Eduardo Akira da Rosa Miyamoto

import matplotlib.pyplot as plt

# 1-Definir a classe do Livro
# Criando Classe Livro
class Livro_class():
    def __init__(self, titulo, autor, genero, quantidade_disponivel):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade_disponivel = quantidade_disponivel

    # Transformando todos os dados em string para que fique legível para quem for usar o programa.
    def __str__(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}, Gênero: {self.genero}, Quantidade Disponível: {self.quantidade_disponivel}"

# 2-Criar a lista de livros
# Lista livros vazia para guardar os livros que serão cadastrados.
livros_cadastrados = []

# 3-Implementar funções para gerenciar os livros

# Cria função para cadastrar um novo livro
def adiciona_livro(titulo, autor, genero, quantidade_disponivel):
    novo_livro = Livro_class(titulo, autor, genero, quantidade_disponivel)
    livros_cadastrados.append(novo_livro)
    print(f"\n📚 O livro com titulo '{titulo}' foi adicionado com sucesso !")

# Campo de entrada dos dados que serão digitados pelo usuário.
def cadastrar_livro():
    print("\n********************************************")
    print("CADASTRO DE LIVROS")
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    genero = input("Digite o gênero do livro: ")
    try:
      quantidade_disponivel = int(input("Digite a quantidade disponível do livro: "))
      adiciona_livro(titulo, autor, genero, quantidade_disponivel)
      print("\n********************************************")
    except ValueError:
      print("\n⚠️Erro? O valor digitado deve ser um número inteiro. Tente novamente!.⚠️")

# Função mostra todos os livros, pega o Livro que está dentro da listra livros_cadastrados.
def mostra_todos_livros():
    for livro in livros_cadastrados:
        print(livro)

# Função mostra livro pelo título
def mostra_livro_por_titulo(titulo):
    for livro in livros_cadastrados:
        if livro.titulo.lower() == titulo.lower():
            print(livro)
            return
    print("Livro não encontrado")


# 4-Utilizar a biblioteca Matplotlib para gerar um gráfico
# Gerar o gráfico de quantidade de livros por gênero
# Dados
def grafico_livros_por_genero():
  if not livros_cadastrados:
    print("\n⚠️Não encontramos nenhum livro cadastrado para gerar o gráfico.⚠️")
    return

  # Dicionário para armazenar a contagem de livros por gênero
  contagem_por_generos = {}

  #Conta a quantidade por gênero
  for livro in livros_cadastrados:
      genero = livro.genero
      quantidade = livro.quantidade_disponivel
      if genero in contagem_por_generos:
          contagem_por_generos[genero] += quantidade
      else:
          contagem_por_generos[genero] = quantidade

  # Preparar os dados para o gráfico
  generos = list(contagem_por_generos.keys())
  quantidades = list(contagem_por_generos.values())

  # Criar o gráfico de barras
  plt.bar(generos, quantidades)
  plt.xlabel('Gênero')
  plt.ylabel('Quantidade de Livros')
  plt.title('Quantidade de Livros por Gênero')
  plt.yticks(quantidades)

  # loop para adicionar um texto de quantidade no topo de cada barra
  for i, quantidade in enumerate(quantidades):
    plt.text(i, quantidade, str(quantidade), ha='center', va='bottom', fontsize=12)
  plt.show()

# Criamos aqui um menu para facilitar para o usuário
def menu():
  while True:
    print("\n============================================================")
    print("\n👋 Seja bem vindo ao sistema de Gerenciamento de Livros 👋")
    print("\n ↗️Escolha uma opção do menu")
    print("\n🔽MENU")
    print("1 - Adicionar livro")
    print("2 - Mostrar todos os livros")
    print("3 - Mostrar livro por título")
    print("4 - Ver gráfico de livros por gênero")
    print("0 - Sair")
    print("\n============================================================")

    escolhas = input("Escolha uma opção: ")
    print(f"\n✅ Número {escolhas} foi digitado")
    print("\n============================================================")

    if escolhas == "1":
      cadastrar_livro()
    elif escolhas == "2":
      mostra_todos_livros()
    elif escolhas == "3":
      busca_titulo = input("Digite o título do livro:")
      mostra_livro_por_titulo(busca_titulo)
    elif escolhas == "4":
      grafico_livros_por_genero()
    elif escolhas == "0":
      print("Saindo do programa. Até a próxima!")
      break
    else:
      print("Opção Inválida! Tente novamente.")
      # Aqui o loop vai perguntar para a pessoa se ela quer voltar ao menu Principal
    continuar = input("\n🔄Voltar ao menu Principal? (S para sim ou qualquer outra tecla para sair): ")
    if continuar.lower() != "s":
      print("\n🙋‍♂️Saindo do programa. Até a próxima!🙋‍♂️")
      break

# Chamando a função para cadastrar um livro antecipado
adiciona_livro("Cosmos", "Carl Sagan", "Ciência", 15)
adiciona_livro("A Origem das Espécies", "Charles Darwin", "Ciência", 20)
adiciona_livro("O Universo Numa Casca de Noz", "Stephen Hawking", "Ciência", 5)
adiciona_livro("Uma Breve História do Tempo", "Stephen Hawking", "Ciência", 12)
adiciona_livro("Sapiens", "Yuval Noah Harari", "Ciência", 25)

adiciona_livro("As Institutas", "João Calvino", "Religião", 15)
adiciona_livro("A Ética Protestante e o Espírito do Capitalismo", "Max Weber", "Religião", 8)
adiciona_livro("Conhecendo a Deus", "J.I. Packer", "Religião", 12)
adiciona_livro("Cinco Pontos", "John Piper", "Religião", 7)
adiciona_livro("Oração", "Timothy Keller", "Religião", 10)

adiciona_livro("A Startup Enxuta", "Eric Ries", "Negócios", 14)
adiciona_livro("O Lado Difícil das Situações Difíceis", "Ben Horowitz", "Negócios", 9)
adiciona_livro("Pai Rico, Pai Pobre", "Robert Kiyosaki", "Negócios", 20)
adiciona_livro("Como Fazer Amigos e Influenciar Pessoas", "Dale Carnegie", "Negócios", 16)
adiciona_livro("O Investidor Inteligente", "Benjamin Graham", "Negócios", 11)

adiciona_livro("A Era das Máquinas Inteligentes", "Ray Kurzweil", "Tecnologia", 6)
adiciona_livro("Código Limpo", "Robert C. Martin", "Tecnologia", 20)
adiciona_livro("A Quarta Revolução Industrial", "Klaus Schwab", "Tecnologia", 8)
adiciona_livro("O Design do Dia a Dia", "Donald Norman", "Tecnologia", 13)
adiciona_livro("O Capital no Século XXI", "Thomas Piketty", "Tecnologia", 19)

# Iniciando Menu
menu()
