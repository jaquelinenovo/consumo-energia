# ⚡ Calculadora de Consumo Elétrico

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-black?logo=github\&logoColor=white)
![Energia](https://img.shields.io/badge/Energia-Consumo%20Elétrico-yellow)

## Objetivo

A **Calculadora de Consumo Elétrico** é um programa desenvolvido em Python que calcula uma estimativa do consumo de energia elétrica de um aparelho durante um mês.

Para realizar o cálculo, o usuário informa:

* Nome do aparelho
* Potência em watts (W)
* Tempo médio de uso por dia, em horas

Além do consumo mensal, o programa também calcula uma estimativa de custo utilizando o valor de **R$ 0,75 por kWh**.

## Linguagem utilizada

O projeto foi desenvolvido utilizando **Python**.

## Fórmula utilizada

O consumo mensal é calculado através da seguinte fórmula:

```text
consumoMensal = (potencia × horasDia × 30) / 1000
```

Onde:

* **potencia** = potência do aparelho em watts (W)
* **horasDia** = quantidade média de horas de uso por dia
* **30** = quantidade estimada de dias no mês
* **1000** = conversão de Wh para kWh

Para calcular o custo:

```text
custo = consumoMensal × 0,75
```

O valor de **R$ 0,75 por kWh** é apenas um valor fixo utilizado como exemplo na atividade.

## Como executar

1. Tenha o Python 3 instalado.
2. Baixe ou clone este repositório.
3. Abra a pasta do projeto no terminal.
4. Execute:

```bash
python app.py
```

5. Informe os dados solicitados pelo programa.

## Exemplo

Considerando um aparelho com potência de **500 W**, utilizado durante **3 horas por dia**:

```text
(500 × 3 × 30) / 1000 = 45 kWh/mês
```

Resultado:

```text
Aparelho: Exemplo
Consumo estimado: 45.00 kWh/mês
Custo estimado: R$ 33.75/mês
```

## Estrutura do projeto

```text
consumo-energia/
├── app.py
└── README.md
```

## Tecnologias

* Python
* GitHub
* Shields.io
* Cálculo de consumo de energia

## Sobre o projeto

Projeto desenvolvido como atividade de iniciação em tecnologia, com o objetivo de praticar programação em Python, organização de arquivos e publicação de projetos no GitHub.
