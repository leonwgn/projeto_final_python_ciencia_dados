# 📊 Análise do Desenvolvimento Humano e Econômico Global

Projeto desenvolvido como parte da disciplina **Python para Ciência de Dados**, do curso de **Pós-Graduação em Inteligência Artificial e Aprendizado de Máquina** da **PUC Minas**.

---

## 📚 Informações Acadêmicas

- **Curso:** Pós-Graduação em Inteligência Artificial e Aprendizado de Máquina
- **Instituição:** PUC Minas
- **Disciplina:** Python para Ciência de Dados
- **Professor:** Leandro Figueira Lessa

### Alunos

- **1471280** - Leon Wagner Farias de Souza - 1471280@sga.pucminas.br
- **1666114** - Marcos Silva de Castro - 1666114@sga.pucminas.br
- **1665824** - Victor Paiva Nevola - 1665824@sga.pucminas.br
- **1669007** - Kelvin de Lucca Feltrin - 1669007@sga.pucminas.br

---

## 🎯 Objetivo do Projeto

Este projeto tem como objetivo realizar uma **Análise Exploratória de Dados (EDA)** utilizando Python, com foco em indicadores históricos de:

- Desenvolvimento humano
- Saúde
- Economia
- Demografia
- Educação

A partir do dataset **Gapminder**, foram realizadas análises estatísticas e visuais para investigar relações entre indicadores socioeconômicos e de qualidade de vida em diversos países ao longo de várias décadas.

Como complemento, foram integrados dados da **UNDP (Programa das Nações Unidas para o Desenvolvimento)** para enriquecer a análise com indicadores de **educação e desenvolvimento humano**.

---

## 📂 Dataset Utilizado

### Gapminder

Dataset amplamente utilizado em estudos de desenvolvimento global, contendo informações históricas sobre:

- `country` → País
- `continent` → Continente
- `year` → Ano
- `lifeExp` → Expectativa de vida
- `gdpPercap` → PIB per capita
- `pop` → População

**Cobertura:** aproximadamente 140 países entre **1952 e 2007**

---

### UNDP (Complementar)

Base complementar utilizada para enriquecer a análise com:

- **Expected Years of Schooling (years)**

Esse indicador permitiu adicionar uma dimensão educacional à análise de desenvolvimento humano.

---

## 📊 Análises Realizadas

O projeto está dividido em blocos temáticos:

### BLOCO 1 — Desenvolvimento Humano Global

- Evolução da média da expectativa de vida ao longo dos anos
- Distribuição da expectativa de vida (1952 vs 2007)
- Países com expectativa de vida acima de 80 anos

---

### BLOCO 2 — Economia e Desenvolvimento

- Relação entre PIB per capita e expectativa de vida
- Evolução do PIB per capita por continente
- Identificação de outliers econômicos

---

### BLOCO 3 — População e Distribuição

- Top 10 países mais populosos
- Ásia vs Europa (crescimento populacional)
- População mundial por continente (área empilhada)

---

### BLOCO 4 — Comparações Regionais

- Distribuição da expectativa de vida por continente (Boxplot)
- Brasil vs média da América do Sul

---

### BLOCO 5 — Relações Estatísticas

- População vs PIB per capita
- Heatmap de correlação entre variáveis

---

### BLOCO 6 — Evolução Histórica

- País com maior crescimento percentual em expectativa de vida (1952 → 2007)

---

### Seção Extra — Educação, Renda e Qualidade de Vida

Integração com dados da **UNDP**, analisando:

- PIB per capita vs expectativa de vida com escolaridade
- Escolaridade vs expectativa de vida

---

## 🏗️ Estrutura do Projeto

```text
projeto_final_python_ciencia_dados/
│
├── app.py                  # Dashboard Streamlit
├── notebook.ipynb          # Análise completa em Jupyter Notebook
│
├── src/
│   ├── charts.py           # Funções modulares de gráficos
│   ├── utils.py            # Tratamento e preparação de dados
│
├── data/
│   └── raw/
│       ├── gapminder.csv
│       └── hdr-data.csv
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **Streamlit**
- **Jupyter Notebook**

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd projeto_final_python_ciencia_dados
```

---

### 2. Criar ambiente virtual

#### Mac / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## ▶️ Executar via Jupyter Notebook

```bash
jupyter notebook
```

Abrir:

```text
notebook.ipynb
```

---

## 🌐 Executar via Streamlit

```bash
streamlit run app.py
```

O dashboard será aberto automaticamente no navegador em:

```text
http://localhost:8501
```

---

## 📌 Observações sobre a Entrega

O projeto foi desenvolvido com suporte a **dois modos de execução**:

### Jupyter Notebook

Modo completo de análise exploratória e desenvolvimento.

### Streamlit Dashboard

Modo interativo de apresentação dos resultados, com navegação por seções e visualização organizada dos gráficos e insights.

---

## 📈 Principais Conclusões

A análise evidenciou que:

- A expectativa de vida global cresceu significativamente entre 1952 e 2007
- Países com maior renda tendem a apresentar maior longevidade
- Crescimento econômico isolado não garante desenvolvimento humano
- Persistem desigualdades regionais significativas entre continentes
- Educação apresenta forte associação com expectativa de vida e qualidade de vida
- Desenvolvimento humano é resultado de múltiplos fatores interligados

---

## 📄 Licença

Projeto desenvolvido para fins **acadêmicos e educacionais**.