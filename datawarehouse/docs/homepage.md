{% docs __overview__ %}

#DBT-Core project ro Data Warehouse of Commodities

This project uses dbt (data build tool) to manage and to transform data
from a commodities Data Warehouse. The goal  is to make a data pipeline efficient
that organize and transform commodities data and transaction to analysis.

## Project Structure

```mermaid
graph TD;
    A[Início] --> B[Extrair Dados das Commodities]
    B --> C[Transformar Dados das Commodities]
    C --> D[Carregar Dados no PostgreSQL]
    D --> E[Fim]

    subgraph Extrair
        B1[Buscar Dados de Cada Commodity]
        B2[Adicionar Dados na Lista]
    end

    subgraph Transformar
        C1[Concatenar Todos os Dados]
        C2[Preparar DataFrame]
    end

    subgraph Carregar
        D1[Salvar DataFrame no PostgreSQL]
    end

    B --> B1
    B1 --> B2
    B2 --> C
    C --> C1
    C1 --> C2
    C2 --> D
    D --> D1
```



### 1. Seeds

### 2. Models

#### Staging

```plaintext
├── models
│   ├── staging
│   │   ├── stg_commodities.sql
│   │   └── stg_movimentacao_commodities.sql
│   └── datamart
│       └── dm_commodities.sql
├── seeds
│   └── movimentacao_commodities.csv
├── dbt_project.yml
└── README.md
```

#### Staging


- **stg_commodities.sql**

- **stg_movimentacao_commodities.sql**

#### Datamart


{% enddocs %}