# Unidade 4 - Normalização de Dados

**Aluno:** Eduardo Akira da Rosa Miyamoto  
**RA:** 2025******  
**Curso:** CyberSecurity  
**Disciplina:** Modelagem de Dados  
**Professor:** Kariston Stevan Luiz  
**Local:** Toyokawa - Japão  
**Ano:** 2025  

---

## Descrição do Trabalho

Nesta Unidade, o objetivo foi aplicar os conceitos de **normalização de dados** em um cenário de **livraria online**, transformando tabelas da **Primeira Forma Normal (1FN)** para a **Segunda Forma Normal (2FN)**.  

O trabalho consistiu em:

- Identificação de dependências parciais nas tabelas **Pedidos, Produtos e Clientes**.  
- Decomposição da tabela `Pedidos` para eliminar redundâncias, criando a tabela associativa `PedidoDetalhes`.  
- Garantia de que todos os atributos não-chave dependam totalmente da chave primária.  
- Criação de um **Diagrama Entidade-Relacionamento (DER)** representando as tabelas normalizadas.  
- Uso do **MySQL Workbench** para modelagem e organização das tabelas.  

---

## Estrutura do Banco de Dados Final (2FN)

- **Clientes**  
  - ClienteID (PK), NomeCliente, EndereçoEntrega  

- **Produtos**  
  - ProdutoID (PK), NomeProduto, Categoria, PreçoUnitário  

- **Pedidos**  
  - PedidoID (PK), ClienteID (FK)  

- **PedidoDetalhes**  
  - PedidoID (PK, FK), ProdutoID (PK, FK), Quantidade, PreçoUnitário  

---

## Ferramentas Utilizadas

- **MySQL Workbench**: modelagem do DER e manipulação de tabelas SQL.  
- **Editor de PDF**: documentação final do relatório.  

---

## Objetivos de Aprendizagem

1. Compreender e aplicar os conceitos de normalização de dados.  
2. Identificar dependências parciais e eliminar redundâncias em tabelas relacionais.  
3. Criar tabelas normalizadas garantindo integridade e consistência dos dados.  
4. Utilizar o MySQL Workbench como ferramenta prática de modelagem de bancos de dados.  

---

## Referências

- MACHADO, Felipe Nery Rodrigues. *Banco de Dados: Projeto e Implementação.* 4. ed. Rio de Janeiro: Érica, 2020. Disponível em: [Minha Biblioteca](https://app.minhabiblioteca.com.br/reader/books/9788536532707/pageid/176)  
- LEAL, Gislaine Camila Lapasini. *Linguagem, programação e banco de dados: guia prático de aprendizagem.* 1. ed. Rio de Janeiro: InterSaberes, 2015. Disponível em: [bVirtual](https://plataforma.bvirtual.com.br/Leitor/Publicacao/30495/epub/136?code=....)  
- BACONLINE. *O que é a normalização de bases de dados e como fazê-la.* E-BAC Online, 01 jun. 2023. Disponível em: [E-BAC Online](https://ebaconline.com.br/blog/normalizacao-de-bases-de-dados)  

---

**Observação:** Todos os códigos e arquivos estão disponíveis no GitHub do aluno: [https://github.com/akiramiyamoto-dev](https://github.com/akiramiyamoto-dev)
