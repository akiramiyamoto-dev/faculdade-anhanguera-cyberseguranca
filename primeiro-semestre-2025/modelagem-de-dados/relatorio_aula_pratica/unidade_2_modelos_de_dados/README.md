# Unidade 2 - Modelos de Bancos de Dados

**Aluno:** Eduardo Akira da Rosa Miyamoto  
**RA:** RA2025****  
**Disciplina:** Modelagem de Dados  
**Unidade:** 2  
**Professor:** Kariston Stevan Luiz  
**Curso:** CyberSecurity  
**Local:** Toyokawa, Japão  
**Ano:** 2025

---

## Descrição do Trabalho

Esta unidade aborda a **Modelagem de Dados**, etapa essencial para a construção de um banco de dados estruturado e organizado. O foco principal do trabalho foi nos **elementos do modelo Entidade-Relacionamento (ER)**, fundamentais para garantir que o sistema seja funcional, consistente e livre de ambiguidades.

O projeto consistiu na criação de um **Diagrama Entidade-Relacionamento (DER)** para a empresa fictícia **MoveRent**, que controla a locação de ciclomotores por clientes e os trajetos percorridos.

---

## Objetivos

- Identificar entidades, atributos e relacionamentos;
- Definir chaves primárias (PK) e estrangeiras (FK);
- Determinar cardinalidade dos relacionamentos;
- Modelar o DER no **MySQL Workbench**;
- Aplicar conceitos de normalização e integridade referencial.

---

## Entidades e Atributos

1. **Pessoa**  
   - CPF (PK), nome, email, telefone
2. **Ciclomotor**  
   - IDCM (PK), nome, ano, cor
3. **Locação**  
   - IDLOC (PK), data, hora, local  
   - CPF (FK) referenciando Pessoa  
   - IDCM (FK) referenciando Ciclomotor
4. **Trajeto**  
   - IDTRAJETO (PK), data, hora, local  
   - IDLOC (FK) referenciando Locação

---

## Relacionamentos e Cardinalidade

- **Pessoa → Locação:** 1:N  
- **Ciclomotor → Locação:** 1:N  
- **Locação → Trajeto:** 1:N  

---

## Ferramentas Utilizadas

- **MySQL Workbench:** Ferramenta visual para modelagem de dados, criação de tabelas, definição de chaves, relacionamentos e visualização do DER.  
  [Site Oficial do MySQL Workbench](https://www.mysql.com/products/workbench/)

- **SQL:** Linguagem utilizada para implementação do modelo relacional.

---

## Arquivos Contidos

- `AtividadePratica_Unidade2_ModelosdeBancosdeDados_EduardoAkiradaRosaMiyamoto.pdf`  
  PDF contendo a descrição detalhada da atividade, desenvolvimento, DER e resultados da Unidade 2.

---

## Resultados de Aprendizagem

- Compreensão do MySQL Workbench e suas funcionalidades básicas;  
- Criação de um DER funcional contemplando as entidades Pessoa, Ciclomotor, Locação e Trajeto;  
- Representação clara de um banco de dados relacional com integridade referencial;  
- Entrega do DER em arquivo PDF, incluindo descrição das entidades, atributos, chaves primárias e estrangeiras, relacionamentos e cardinalidades.

---

## Conclusão

O trabalho permitiu aplicar conceitos teóricos de modelagem de dados na prática, desenvolvendo habilidades essenciais para a construção de sistemas de banco de dados estruturados e consistentes.

---

## Referências

1. MACHADO, Felipe Nery Rodrigues. *Banco de Dados: Projeto e Implementação.* 3. ed. São Paulo: Érica, 2010.  
2. DEVMedia. *MER e DER: modelagem de bancos de dados.* Disponível em: [https://www.devmedia.com.br/mer-e-der-modelagem-de-bancos-de-dados/14332](https://www.devmedia.com.br/mer-e-der-modelagem-de-bancos-de-dados/14332). Acesso em: 24 set. 2025.  
3. PINTO, Pedro. *Como criar um Diagrama EER com o MySQL Workbench.* Pplware, 19 out. 2015. Disponível em: [https://pplware.sapo.pt/software/como-criar-um-diagramaeer-com-o-mysql-workbench/](https://pplware.sapo.pt/software/como-criar-um-diagramaeer-com-o-mysql-workbench/). Acesso em: 24 set. 2025.
