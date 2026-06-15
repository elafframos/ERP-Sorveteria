# 🍦 ERP-Sorveteria — Backend

> **REST API for POS and Inventory Management** | API REST para PDV e Gestão de Estoque

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django_REST_Framework-ff1709?logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Deploy](https://img.shields.io/badge/deploy-railway-blueviolet?logo=railway)](https://railway.app/)

---

## 📋 Sobre o projeto | About

**PT-BR:** API REST que serve como backend completo do sistema de gestão da **Picolé Super +**. Responsável pela autenticação segura, gerenciamento de mais de **3.000 itens** no estoque, registro de vendas e toda a lógica de negócio da operação. Desenvolvido com Django REST Framework e PostgreSQL, com deploy em produção na Railway.

**EN:** REST API serving as the complete backend for the **Picolé Super +** management system. Handles secure authentication, inventory management of over **3,000 items**, sales records, and all business logic. Built with Django REST Framework and PostgreSQL, deployed to production on Railway.

---

## ⚡ Destaques técnicos | Technical Highlights

- **Token Authentication** — autenticação segura via Django Token Auth em todos os endpoints protegidos
- **Gestão de alta volumetria** — arquitetura de dados otimizada para consultas instantâneas em catálogos com mais de 3.000 itens
- **Identificadores Únicos Compostos** — lógica customizada para resolver conflito de códigos de barras duplicados, permitindo rastreio individual por sabor
- **Arquitetura MVT** — separação clara entre models, views e serializers seguindo boas práticas do Django
- **Variáveis de ambiente** — configuração via Dotenv para separação segura entre ambientes de desenvolvimento e produção

---

## 🛠️ Tecnologias | Tech Stack

| Camada | Tecnologia |
|--------|-----------|
| Linguagem | Python |
| Framework | Django + Django REST Framework |
| Banco de Dados | PostgreSQL |
| Autenticação | Django Token Auth |
| Deploy | Railway |
| Versionamento | Git & GitHub |
| Variáveis de ambiente | Dotenv (.env) |

---

## 🔗 Repositório do Frontend

Este projeto é o backend da aplicação. O frontend (React.js) está disponível em:
👉 [sorvesystem-frontend](https://github.com/elafframos/sorvesystem-frontend)

🔗 **Demo ao vivo:** [sorvesystem-frontend.vercel.app](https://sorvesystem-frontend.vercel.app/)

---

## 🚀 Como rodar localmente | How to run locally

```bash
# Clone o repositório
git clone https://github.com/elafframos/ERP-Sorveteria.git

# Entre na pasta
cd ERP-Sorveteria

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o .env com suas credenciais do banco de dados

# Rode as migrations
python manage.py migrate

# Inicie o servidor
python manage.py runserver
```

---

## 🔐 Autenticação | Authentication

A API utiliza Token Authentication. Para acessar os endpoints protegidos, inclua o token no header da requisição:

```
Authorization:
```

> Credenciais de teste disponíveis mediante solicitação.

---

## 👨‍💻 Autor | Author

**Élaff Ramos** — [LinkedIn](https://linkedin.com/in/elaff-ramos) · [GitHub](https://github.com/elafframos) · [Portfólio](https://portifolio-elafframos.vercel.app)
