Calculadora de Consumo Elétrico

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![GitHub](https://img.shields.io/badge/GitHub-Reposit%C3%B3rio-black?logo=github)](https://github.com/)
[![Energia](https://img.shields.io/badge/Energia-Consumo%20el%C3%A9trico-yellow)](#)

Objetivo

A **Calculadora de Consumo Elétrico** é um programa desenvolvido em Python para estimar quanto um aparelho elétrico consome de energia por mês, usando informações simples de uso.

O usuário informa:
- Nome do aparelho;
- Potência do aparelho em watts (W);
- Tempo médio de uso diário em horas.

O programa calcula o consumo mensal estimado em **kWh/mês** e também apresenta uma estimativa de custo usando o valor fixo de **R$ 0,75 por kWh**.

Linguagem utilizada

O projeto foi desenvolvido em **Python**.

Fórmula utilizada

O consumo mensal é calculado pela fórmula:

`consumoMensal = (potência × horasDia × 30) / 1000`

- **potência:** potência do aparelho em watts (W);
- **horasDia:** média de horas de uso por dia;
- **30:** estimativa de dias de uso no mês;
- **1000:** conversão de Wh para kWh.

O custo estimado é calculado por:

`custo = consumoMensal × 0,75`

> O valor de R$ 0,75/kWh é apenas um valor fixo de exemplo, conforme a proposta da atividade. O valor real da tarifa pode variar.

Como executar

1. Tenha o Python 3 instalado.
2. Baixe ou clone este repositório.
3. Abra a pasta do projeto no terminal.
4. Execute:

```bash
python app.py
```

5. Informe os dados solicitados pelo programa.

Exemplo

Se um aparelho tiver potência de **500 W** e for usado por **3 horas por dia**:

`(500 × 3 × 30) / 1000 = 45 kWh/mês`

Resultado esperado:

```text
Aparelho: Exemplo
Consumo estimado: 45.00 kWh/mês
Custo estimado: R$ 33.75/mês
```

Estrutura do projeto

```text
consumo-energia/
├── app.py
└── README.md
```

##Tecnologias

-  Python
-  GitHub
-  Cálculo de consumo de energia
