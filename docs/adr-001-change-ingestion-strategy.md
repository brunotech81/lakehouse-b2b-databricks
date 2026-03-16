# ADR-001: Alteração na Estratégia de Ingestão de Dados

## Status
Aprovado

## Contexto

O plano inicial do projeto previa a seguinte arquitetura:

Python (VS Code)  
↓  
Azure Blob Storage (Landing Zone)  
↓  
Databricks (Processamento)

No entanto, devido a limitações de licença e restrições do ambiente Azure, não foi possível manter o armazenamento intermediário no Azure Blob Storage.

## Decisão

Adotar temporariamente a seguinte estratégia:

Python (VS Code)  
↓  
Upload direto no Databricks (Workspace)  
↓  
Processamento com PySpark

O Azure Blob Storage permanece documentado como arquitetura alvo futura.

## Justificativa

- Redução de custos e dependência de serviços pagos
- Limitações técnicas do ambiente disponível
- Foco principal do projeto: aprendizado em Databricks e PySpark
- Manutenção da arquitetura Medallion (RAW → BRONZE → GOLD)

## Consequências

Positivas:
- Maior velocidade de desenvolvimento
- Simplificação do ambiente
- Continuidade do aprendizado prático

Negativas:
- Perda temporária da simulação completa de Data Lake na Azure
- Arquitetura parcialmente simplificada

## Próximos Passos

- Manter organização RAW no Databricks
- Evoluir pipeline para Bronze, Silver e Gold
- Futuramente reavaliar integração com Azure Blob Storage
