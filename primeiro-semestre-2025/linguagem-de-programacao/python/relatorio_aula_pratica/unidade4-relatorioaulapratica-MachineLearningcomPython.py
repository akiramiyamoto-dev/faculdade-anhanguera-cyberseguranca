# ROTEIRO DE AULA PRÁTICA
# NOME DA DISCIPLINA: Linguagem de Programação
# Unidade: 4 – Aplicações com Python
# Aula: 4 – Machine Learning com Python
# Author: Eduardo Akira da Rosa Miyamoto

# Importar bibliotecas
import numpy as np
import tensorflow as tf
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras

# Carregar conjunto de dados Iris
iris = load_iris()
X = iris.data
y = iris.target

# Passo 2: Pré-processamento dos Dados
# X representa a entrada dos dados
# y representa variável dependente, que queremos prever
# test_size faz com que os 20% dos dados vão para o conjunto de teste, e o restante ficam para o treino
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar os dados.
# Ajuda a rede neural a treinar de forma mais estável e rápida
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Passo 3: Construir o Modelo
# Rede neural simples(4 neurônios, camada oculta com 10 neurônios e ativação ReLu (Rectified Linear Unit)e saída com 3 neurônios(3 espécies) )
# Rectified Linear Unit, é usada para introduzir não-linearidade no modelo, o que é essencial para que a rede consiga aprender padrões complexos nos dados.
model = keras.Sequential([
    keras.Input(shape=(4,)),
    keras.layers.Dense(10, activation='relu'),
    keras.layers.Dense(3, activation='softmax')
])

# Passo 4: Treinar o Modelo
# Ajusta os parâmetros para aprender a classificar corretamente as espécies
# o método .compile() serve para configurar como o modelo será treinado, não começa o treinamento apenas define as regras de aprendizado.
# Dentro do compile, passamos três coisas principais: otimizador, função de perda(loss function) e métricas de avaliação.
# "optimizer='adam'" é o "cérebro" que decide como ajustar os pesos da rede neural para melhorar o aprendizado.
# "adam" é um dos mais usados porque combina velocidade e boa precisão. (ajusta automaticamente a taxa de aprendizado, facilitando convergir para uma boa solução.)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Passo 5: Avaliar o Modelo
# 50 épocas significa que ele repetirá o treino 50 vezes
# Com esses valores o modelo será treinado sem que perca a capacidade de ir aprendendo mais, assim ele não vicia em um tipo de dados.
# validation_split=0.2 separa automaticamente 20% do conjunto de treino para validação durante as épocas.
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=0)
loss, accuracy = model.evaluate(X_test, y_test)
print(f'✅ Acurácia no conjunto de teste: {accuracy * 100:.2f}%')

# Passo 6 - Fazer Previsões
# Aqui cada previsão retorna a probabilidade de pertencimento a cada classe, e pode-se extrair a classe mais provável usando argmax.
predictions = model.predict(X_test)
predicted_classes = tf.argmax(predictions, axis=1).numpy()

# Aqui na variável "class_names" será atribuído os nomes das espécies que existem no dataset Iris: ['setosa','versicolor','virginica']
class_names = iris.target_names
print("\n")
print("=="*50)
print("Criando um modelo de Machine Learning".center(100))
print("=="*50)
print("\n📊 Comparação entre valores reais e previstos:")
for real, previsto in zip(y_test, predicted_classes):
    print(f" - Real: {class_names[real]}  |  Previsto: {class_names[previsto]}")

# Contagem de previsões por classe (quem foi mais previsto)
unique, counts = np.unique(predicted_classes, return_counts=True)
print("\n🏆 Quantidade de previsões por espécie:")
pred_count_map = {class_names[u]: c for u, c in zip(unique, counts)}
for name in class_names:
    # se a espécie não apareceu nas previsões, mostra zero
    cnt = pred_count_map.get(name, 0)
    print(f" - {name:10s}: {cnt} vezes")

# Vencedora = espécie mais prevista
if len(counts) > 0:
    vencedora_idx = unique[np.argmax(counts)]
    vencedora = class_names[vencedora_idx]
    print(f"\n🌸 Espécie mais prevista pelo modelo (vencedora): {vencedora}")
else:
    print("\n🌸 Nenhuma previsão encontrada.")


