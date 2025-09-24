#Unidade: 1 – INTRODUÇÃO A LINGUAGEM PYTHON
#Aula: 4 - FUNÇÕES_EM_PYTHON
#author: Eduardo Akira da Rosa Miyamoto
#curso: Cybersecurity
#Faculdade Anhanguera - EAD

# Título do Sistema
print("====> Bem-vindo ao Sistema de Gestão de Notas! <====")
print(" Pronto para saber o seu resultado ?\n")

# Input para guardar o nome do aluno
aluno = input(" Insira o nome do aluno: ")
print(f">>> Olá, {aluno}\n")

# Variavel para guardar as notas em lista
notas = []

# Por serem 4 notas, usamos o laço for com range(4) - faz que o laço de código se repita apenas 4 vezes
# Com o append, guardamos essas informações das notas na lista notas[]

for i in range(4):
  # Usamos o while com try e except para garantir apenas notas válidas, com casas decimais
  while True: 
      try:      
          insere_Nota = float(input(f"Insira a nota {i+1}: "))
          if 0.0 <= insere_Nota <=10.0:
            notas.append(insere_Nota)
            break
          else:
              print("⚠️Nota inválida. Por favor, insira uma nota entre 0 e 10.")
      except ValueError:
          print("⚠️Entrada inválida. Por favor, insira um número válido.")

# Criamos uma função para calcular a média.
def calcular_media(notas):
  total = sum(notas)
  media = total / len(notas)
  return media

# Uma função lambda para arredondar a média para duas casas decimais
arredondar_media = lambda media: round(media, 2)

# Calcula a média e usa função de arredondamento da média
media = calcular_media(notas)
media_arredondada = arredondar_media(media)

# Função para determinar a situação do aluno(aprovado ou reprovado)
def determinar_situacao(media):
  if media >= 7:
    return f"👏👏👏 Parabéns, o aluno está aprovado !!! 👏👏👏"
  else:
    return f"😭😭😭 Infelizmente, o aluno está reprovado!!! 😭😭😭 <Se esforce mais!!!>"

# Relatório final com todas as informações.
print("\n" + "="*40)
print("\n========= Relatório Final ! ============")
print(f"{'Aluno': <20} >>> {aluno}")
print(f"{'Notas inseridas': <20} >>> {notas}")
print(f"{'Média':<20} >>> {media_arredondada:.2f}")
print(f"{'Situação do aluno': <20} >>> {determinar_situacao(media)}")
print("\nObrigado por usar o nosso Sistema de Gestão de Notas\n")
print("="*40)

