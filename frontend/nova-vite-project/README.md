📘 Nova Coworking
Sistema de Gestão de Salas e Reservas

📦 Versão Estável v1.0

📑 Sumário

📌 Visão Geral

🧱 Arquitetura do Projeto

🔧 Tecnologias Utilizadas

🎯 Objetivo do Sistema

🔐 Regras de Negócio

🗄️ Backend

🧩 Entidades do Sistema

⏰ Regras de Reserva

🔌 Endpoints da API

📑 Swagger

🌐 CORS

▶️ Como Rodar o Backend Localmente

🎨 Frontend

▶️ Como Rodar o Frontend Localmente

🌍 Ambientes (Local x Produção)

⚙️ Deploy em Produção

⚠️ Limitações Atuais

🚀 Evoluções Planejadas

📌 Visão Geral

O Nova Coworking é um sistema web para gestão de salas, usuários e reservas, desenvolvido para:

Coworkings

Escolas

Empresas

Ambientes com espaços compartilhados

O projeto tem foco em:

Arquitetura full stack real

Separação clara entre frontend e backend

Regras de negócio centralizadas no backend

Organização e legibilidade de código

Escalabilidade futura

🧱 Arquitetura do Projeto

O sistema segue o modelo Frontend desacoplado + API REST.

Frontend (React + Vite)
        │
        │ HTTP (Axios / JSON)
        ▼
Backend (FastAPI)
        │
        │ ORM (SQLAlchemy)
        ▼
Banco de Dados (PostgreSQL - Supabase)

Estrutura Geral do Repositório
Nova-Coworking/
├─ backend/
│  ├─ main.py
│  ├─ database.py
│  ├─ models/
│  ├─ schemas/
│  └─ router/
├─ frontend/
│  └─ nova-vite-project/
└─ README.md

🔧 Tecnologias Utilizadas
Backend

Python 3.11.8

FastAPI

SQLAlchemy

Pydantic

PostgreSQL (Supabase)

Uvicorn

CORS Middleware

Frontend

React

Vite

Axios

React Router DOM

CSS puro

🎯 Objetivo do Sistema

Cadastrar usuários administrativos

Cadastrar salas com capacidade e recursos

Criar, listar e excluir reservas

Evitar conflitos de horário

Exibir agenda visual diária

Dashboard com visão geral

📌 O sistema inicia no Dashboard
📌 Não existe página Home

🔐 Regras de Negócio (Decisão Arquitetural)

Toda regra de negócio fica no backend

O frontend não valida conflitos

O frontend apenas envia dados

O backend decide:

Se a reserva é válida

Se existe conflito

Se está dentro do horário permitido

🗄️ Backend
📂 Estrutura
backend/
├─ main.py
├─ database.py
├─ models/
│  ├─ usuarios.py
│  ├─ salas.py
│  └─ reservas.py
├─ schemas/
│  ├─ usuario.py
│  ├─ sala.py
│  └─ reserva.py
└─ router/
   ├─ usuarios.py
   ├─ salas.py
   └─ reservas.py

🧩 Entidades do Sistema
👤 Usuário

id

nome

email

senha (obrigatória)

📌 A senha não é usada atualmente, mas o campo existe por decisão arquitetural visando:

Autenticação futura

JWT

Controle de permissões

🏢 Sala

id

nome

capacidade

recursos

fotourl (opcional)

📅 Reserva

id

usuario_id

sala_id

data_reserva

duração (horas)

status

observacao

⏰ Regras de Reserva (Backend)

Horário permitido: 08:00 às 22:00

Duração mínima: 2 horas

Não permite sobreposição de horários

Conflitos são verificados no backend

🔌 Endpoints da API
Usuários

GET /usuarios

POST /usuarios

PUT /usuarios/{id}

DELETE /usuarios/{id}

Salas

GET /salas

POST /salas

Reservas

GET /reservas

POST /reservas

DELETE /reservas/{id}

📑 Swagger (Documentação da API)

Disponível automaticamente pelo FastAPI:

/docs


Permite:

Testar endpoints

Ver schemas

Simular requisições

🌐 CORS
Local

http://localhost:5173

Produção

https://nova-coworking.vercel.app

▶️ Como Rodar o Backend Localmente
Pré-requisitos

Python 3.11.8

PostgreSQL ou Supabase

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload


API disponível em:

http://127.0.0.1:8000

🎨 Frontend
Estrutura
src/
├─ components/
├─ pages/
├─ services/
├─ App.jsx
├─ main.jsx
└─ App.css

▶️ Como Rodar o Frontend Localmente (Vite)
npm install
npm run dev


Arquivo .env:

VITE_API_URL=http://127.0.0.1:8000


Acesso:

http://localhost:5173

🌍 Ambientes (Local x Produção)
Camada	Local	Produção
Frontend	Vite	Vercel
Backend	FastAPI	Render
Banco	Supabase	Supabase
Python	3.11.8	3.11.8
Variáveis	.env	Dashboard
⚙️ Deploy em Produção
Backend (Render)

O arquivo runtime.txt não funcionou corretamente

A versão do Python precisou ser forçada via variável:

PYTHON_VERSION=3.11.8


Start command:

uvicorn main:app --host 0.0.0.0 --port $PORT

Frontend (Vercel)

Build com Vite

Uso de vercel.json para SPA:

{
  "rewrites": [{ "source": "/(.*)", "destination": "/" }]
}

⚠️ Limitações Atuais

Sem autenticação

Sem permissões

Sem testes automatizados

Layout em evolução

🚀 Evoluções Planejadas

Autenticação JWT

Login público

Permissões

Docker

Testes automatizados

Dashboard avançado

📦 Nova Coworking — Versão Estável v1.0