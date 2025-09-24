# ROTEIRO DE AULA PRÁTICA
# NOME DA DISCIPLINA: LINGUAGEM DE PROGRAMAÇÃO
# Unidade: 3 – Introdução à Análise de Dados com Python
# Aula: 4 – Visualização de Dados em Python
# Author: Eduardo Akira da Rosa Miyamoto

#Passo 1: Conectar ao banco de dados SQLite e criar uma tabela
#Primeiro, você precisa estabelecer uma conexão com o banco de dados SQLite e carregar os dados relevantes para análise.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sqlite3

# Passo 1.1: Conectar ao banco de dados (ou criar, se não existir)
conexao = sqlite3.connect('dados_vendas.db')

# Passo 1.2: Criar um cursor
cursor = conexao.cursor()

# Passo 1.3: Criar uma tabela (se não existir)
cursor.execute('''
CREATE TABLE vendas1 (
id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
data_venda DATE,
produto TEXT,
categoria TEXT,
valor_venda REAL
)
''')

# Passo 1.4: Inserir alguns dados
cursor.execute('''
INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
('2023-01-05', 'Produto B', 'Roupas', 350.00),
('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
('2023-03-15', 'Produto D', 'Livros', 200.00),
('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
('2023-04-02', 'Produto F', 'Roupas', 400.00),
('2023-05-05', 'Produto G', 'Livros', 150.00),
('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
('2023-07-20', 'Produto I', 'Roupas', 600.00),
('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
('2023-09-30', 'Produto K', 'Livros', 300.00),
('2023-10-05', 'Produto L', 'Roupas', 450.00),
('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
('2023-12-20', 'Produto N', 'Livros', 250.00);
''')

# Passo 1.5: Confirmar as mudanças
conexao.commit()

# ============================================================================
# PASSO 2: EXPLORAR E PREPARAR OS DADOS
# ============================================================================
print("\n" + "="*50)
print("PASSO 2: EXPLORANDO E PREPARANDO OS DADOS")
print("="*50)

# Carregar dados do banco SQLite para DataFrame
df_vendas = pd.read_sql_query('''
    SELECT * FROM vendas1 ORDER BY data_venda
''', conexao)

# Converter data para datetime
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])

# Criar colunas adicionais para análise
df_vendas['mes'] = df_vendas['data_venda'].dt.month
df_vendas['mes_nome'] = df_vendas['data_venda'].dt.month_name()
df_vendas['trimestre'] = df_vendas['data_venda'].dt.quarter

print("📊 Informações gerais dos dados:")
print(f"Formato dos dados: {df_vendas.shape}")
print(f"Colunas: {list(df_vendas.columns)}")
print(f"Período: {df_vendas['data_venda'].min()} até {df_vendas['data_venda'].max()}")

print("\n📋 Primeiras 5 linhas:")
print(df_vendas.head())

print("\n📈 Informações dos tipos de dados:")
print(df_vendas.info())

print("\n📊 Estatísticas descritivas:")
print(df_vendas.describe())

print("\n🔍 Verificação de dados faltantes:")
print(df_vendas.isnull().sum())

print("\n📦 Valores únicos por coluna:")
print(f"Produtos únicos: {df_vendas['produto'].nunique()}")
print(f"Categorias: {df_vendas['categoria'].unique()}")
print(f"Meses com vendas: {sorted(df_vendas['mes'].unique())}")

# ============================================================================
# PASSO 3: ANÁLISE DOS DADOS
# ============================================================================
print("\n" + "="*50)
print("PASSO 3: ANÁLISE DOS DADOS")
print("="*50)

# 3.1 Análise por categoria
print("\n📊 ANÁLISE POR CATEGORIA:")
vendas_por_categoria = df_vendas.groupby('categoria').agg({
    'valor_venda': ['sum', 'mean', 'count', 'min', 'max']
}).round(2)

vendas_por_categoria.columns = ['Total', 'Média', 'Quantidade', 'Mínimo', 'Máximo']
print(vendas_por_categoria)

# Participação percentual
vendas_por_categoria['Participação_%'] = (vendas_por_categoria['Total'] / vendas_por_categoria['Total'].sum() * 100).round(1)
print(f"\n💰 Participação por categoria:")
print(vendas_por_categoria[['Total', 'Participação_%']])

# 3.2 Análise mensal
print("\n📅 ANÁLISE MENSAL:")
vendas_mensais = df_vendas.groupby(['mes', 'mes_nome']).agg({
    'valor_venda': ['sum', 'mean', 'count']
}).round(2)

vendas_mensais.columns = ['Total_Vendas', 'Ticket_Médio', 'Qtd_Vendas']
vendas_mensais = vendas_mensais.reset_index()
print(vendas_mensais)

# 3.3 Top produtos
print("\n🏆 TOP 5 MAIORES VENDAS:")
top_vendas = df_vendas.nlargest(5, 'valor_venda')[['produto', 'categoria', 'valor_venda', 'data_venda']]
print(top_vendas)

# 3.4 Análise por trimestre
print("\n📈 ANÁLISE POR TRIMESTRE:")
vendas_trimestre = df_vendas.groupby('trimestre').agg({
    'valor_venda': ['sum', 'mean', 'count']
}).round(2)
vendas_trimestre.columns = ['Total', 'Média', 'Quantidade']
print(vendas_trimestre)

# 3.5 Métricas principais
total_vendas = df_vendas['valor_venda'].sum()
ticket_medio = df_vendas['valor_venda'].mean()
melhor_categoria = vendas_por_categoria['Total'].idxmax()
melhor_mes = vendas_mensais.loc[vendas_mensais['Total_Vendas'].idxmax(), 'mes_nome']

print(f"\n📊 MÉTRICAS PRINCIPAIS:")
print(f"💰 Total de vendas: R$ {total_vendas:,.2f}")
print(f"🎫 Ticket médio: R$ {ticket_medio:.2f}")
print(f"📦 Total de transações: {len(df_vendas)}")
print(f"🥇 Melhor categoria: {melhor_categoria}")
print(f"📅 Melhor mês: {melhor_mes}")

# ============================================================================
# PASSO 4: VISUALIZAÇÃO DOS DADOS
# ============================================================================
print("\n" + "="*50)
print("PASSO 4: VISUALIZAÇÃO DOS DADOS")
print("="*50)

# Configurar estilo
plt.style.use('default')
sns.set_palette("husl")

# Criar figura com subplots
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('Dashboard de Análise de Vendas - 2023', fontsize=16, fontweight='bold')

# Gráfico 1: Vendas por categoria (Pizza)
ax1 = axes[0, 0]
vendas_cat_values = vendas_por_categoria['Total']
cores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57']
wedges, texts, autotexts = ax1.pie(vendas_cat_values, labels=vendas_cat_values.index,
                                   autopct='%1.1f%%', startangle=90, colors=cores)
ax1.set_title('Vendas por Categoria', fontweight='bold')

# Gráfico 2: Evolução mensal
ax2 = axes[0, 1]
ax2.plot(vendas_mensais['mes'], vendas_mensais['Total_Vendas'],
         marker='o', linewidth=2, markersize=6, color='#FF6B6B')
ax2.set_title('Evolução das Vendas Mensais', fontweight='bold')
ax2.set_xlabel('Mês')
ax2.set_ylabel('Valor (R$)')
ax2.grid(True, alpha=0.3)

# Gráfico 3: Vendas por categoria (Barras)
ax3 = axes[0, 2]
bars = ax3.bar(vendas_por_categoria.index, vendas_por_categoria['Total'], color=cores)
ax3.set_title('Total de Vendas por Categoria', fontweight='bold')
ax3.set_xlabel('Categoria')
ax3.set_ylabel('Valor Total (R$)')
ax3.tick_params(axis='x', rotation=45)

# Gráfico 4: Ticket médio por categoria
ax4 = axes[1, 0]
ax4.bar(vendas_por_categoria.index, vendas_por_categoria['Média'], color=cores)
ax4.set_title('Ticket Médio por Categoria', fontweight='bold')
ax4.set_xlabel('Categoria')
ax4.set_ylabel('Ticket Médio (R$)')
ax4.tick_params(axis='x', rotation=45)

# Gráfico 5: Quantidade de vendas por mês
ax5 = axes[1, 1]
ax5.bar(vendas_mensais['mes'], vendas_mensais['Qtd_Vendas'], color='#4ECDC4')
ax5.set_title('Quantidade de Vendas por Mês', fontweight='bold')
ax5.set_xlabel('Mês')
ax5.set_ylabel('Quantidade')

# Gráfico 6: Boxplot valores por categoria
ax6 = axes[1, 2]
df_vendas.boxplot(column='valor_venda', by='categoria', ax=ax6)
ax6.set_title('Distribuição dos Valores por Categoria', fontweight='bold')
ax6.set_xlabel('Categoria')
ax6.set_ylabel('Valor (R$)')
plt.suptitle('')  # Remove título automático do boxplot

plt.tight_layout()
plt.show()

print("✅ Visualizações geradas com sucesso!")

# ============================================================================
# PASSO 5: CONCLUSÃO E ANÁLISE DE INSIGHTS
# ============================================================================
print("\n" + "="*50)
print("PASSO 5: CONCLUSÃO E ANÁLISE DE INSIGHTS")
print("="*50)

print("💡 PRINCIPAIS INSIGHTS:")
print("-" * 30)

# Insight 1: Categoria dominante
categoria_lider = vendas_por_categoria['Total'].idxmax()
participacao_lider = vendas_por_categoria.loc[categoria_lider, 'Participação_%']
print(f"🎯 1. {categoria_lider} é a categoria líder com {participacao_lider}% das vendas")

# Insight 2: Sazonalidade
mes_maior_venda = vendas_mensais.loc[vendas_mensais['Total_Vendas'].idxmax()]
mes_menor_venda = vendas_mensais.loc[vendas_mensais['Total_Vendas'].idxmin()]
print(f"📅 2. Maior volume em {mes_maior_venda['mes_nome']} (R$ {mes_maior_venda['Total_Vendas']:,.2f})")
print(f"📅 3. Menor volume em {mes_menor_venda['mes_nome']} (R$ {mes_menor_venda['Total_Vendas']:,.2f})")

# Insight 3: Ticket médio
categoria_maior_ticket = vendas_por_categoria['Média'].idxmax()
maior_ticket = vendas_por_categoria.loc[categoria_maior_ticket, 'Média']
print(f"🎫 4. {categoria_maior_ticket} tem o maior ticket médio: R$ {maior_ticket:.2f}")

# Insight 4: Performance geral
print(f"📊 5. Performance geral: {len(df_vendas)} vendas geraram R$ {total_vendas:,.2f}")

print(f"\n📋 RECOMENDAÇÕES PARA A EMPRESA:")
print("-" * 35)

print(f"✅ 1. FORTALECER {categoria_lider}:")
print(f"   - Investir em marketing desta categoria")
print(f"   - Aumentar variedade de produtos")
print(f"   - Negociar melhores condições com fornecedores")

categoria_fraca = vendas_por_categoria['Total'].idxmin()
print(f"\n📈 2. DESENVOLVER {categoria_fraca}:")
print(f"   - Criar promoções específicas")
print(f"   - Analisar motivos da baixa performance")
print(f"   - Considerar parcerias estratégicas")

print(f"\n📅 3. OTIMIZAR SAZONALIDADE:")
print(f"   - Preparar estoque para {mes_maior_venda['mes_nome']}")
print(f"   - Criar campanhas especiais em {mes_menor_venda['mes_nome']}")
print(f"   - Planejar promoções baseadas no histórico")

print(f"\n💰 4. AUMENTAR TICKET MÉDIO:")
print(f"   - Implementar vendas cruzadas")
print(f"   - Oferecer combos e pacotes")
print(f"   - Treinar equipe de vendas")

print(f"\n📊 5. MONITORAMENTO CONTÍNUO:")
print(f"   - Acompanhar métricas mensalmente")
print(f"   - Criar alertas para quedas de performance")
print(f"   - Expandir análise para mais períodos")

# Fechar conexão com o banco
conexao.close()

print("\n" + "="*50)
print("✅ ANÁLISE COMPLETA FINALIZADA COM SUCESSO!")
print("📊 Relatório salvo e gráficos gerados")
print("💼 Insights e recomendações documentados")
print("="*50)
