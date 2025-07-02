# 📊 Projetos com Brapi.dev

Este repositório contém projetos em Python utilizando a [Brapi.dev](https://brapi.dev/) — uma API gratuita para acessar dados do mercado financeiro brasileiro, como ações, dividendos, indicadores fundamentalistas e muito mais.

---

## 📦 Estrutura do Projeto

```
brapi-projetos/
│
├── dashboards/           # Dashboards em Streamlit ou Dash
│   └── dashboard_acoes.py
│
├── simuladores/          # Simuladores de dividendos e renda passiva
│   └── simulador_dividendos.py
│
├── dados/                # Dados de exemplo ou carteiras
│   └── carteira_exemplo.json
│
├── utils/                # Funções auxiliares para chamada à API
│   └── brapi_request.py
│
├── requirements.txt      # Bibliotecas necessárias
└── README.md             # Este arquivo
```

---

## 🚀 Exemplos de Aplicações

- 📈 Dashboard interativo com Streamlit
- 🧮 Simulador de dividendos acumulados
- 💰 Monitor de carteira com cálculo de proventos
- 📉 Comparativo histórico de ações (gráficos)

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- [Brapi.dev](https://brapi.dev/)
- Streamlit
- Pandas
- Requests
- Matplotlib / Plotly (opcional)

---

## ▶️ Como Rodar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/brapi-projetos.git
cd brapi-projetos
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Rode um dos projetos:

```bash
streamlit run dashboards/dashboard_acoes.py
```

---

## 🔐 Sobre a API

A Brapi oferece acesso gratuito com limite de requisições. Para maior performance, recomenda-se cache local dos dados em projetos maiores.

Mais informações: [https://brapi.dev/docs](https://brapi.dev/docs)

---

## 📬 Contato

Projeto desenvolvido por **Robert Dethemann Gans**  
Founder da [Gans Academy](https://gans-academy.com) | Professor | Investidor | Criador de soluções em educação financeira e tecnologia.
