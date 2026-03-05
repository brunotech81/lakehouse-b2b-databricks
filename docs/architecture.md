# Arquitetura do Projeto B2B - Lakehouse (simulando empresa real)

## 1. Objetivo

Implementar um Data Lakehouse utilizando Azure Blob Storage como camada de armazenamento bruto (Landing Zone) e Databricks para processamento e transformação dos dados.

## 2. Arquitetura Proposta

Fluxo:

Python (geração de dados)  
↓  
Azure Blob Storage (Landing Zone - Raw Data)  
↓  
Databricks (Ingestão → nikel → Bronze → Silver → Gold)


## 3. Justificativa Técnica

Escolhi o Azure Blob Storage por:

- Baixo custo
- Alta escalabilidade
- Integração nativa com Databricks
- Simplicidade operacional

O foco do projeto é aprendizado prático em Engenharia de dados, priorizando Databricks como motor de processamento.


## 4. Estimativa de Custo

### Cenário Inicial (1 GB)

- Capacidade: 1 GB
- Tier: Hot
- Redundância: LRS
- Custo estimado mensal: ~$0.04

### Cenário de Crescimento (100 GB)

- Capacidade: 100 GB
- Custo estimado mensal: ~$3.27

Observação:
O crescimento é linear e previsível, demonstrando escalabilidade financeira da solução.


## 5. Considerações de Custo

- Upload de dados: Gratuito
- Retrieval (Hot Tier): Sem custo adicional relevante
- Operações: Baixo impacto no cenário atual
- Não há uso de serviços adicionais na Azure


## 6. Escalabilidade

A solução permite crescimento para volumes maiores (TBs) sem alteração significativa da arquitetura, mantendo previsibilidade de custo.


## 7. Próximos Passos

- Criar Storage Account
- Criar container `landing-zone`
- Realizar upload inicial dos dados
- Conectar Databricks ao Blob Storage
