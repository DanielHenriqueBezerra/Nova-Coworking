# 📘 Nova Coworking
## Sistema de Gestão de Salas e Reservas

---

## 📌 Visão Geral

O **Nova Coworking** é um sistema web para gestão de **salas, usuários e reservas**, desenvolvido para:

- Coworkings  
- Escolas  
- Empresas  
- Ambientes que utilizam espaços compartilhados  

O sistema foi projetado com foco em:

- Separação clara entre frontend e backend  
- Regras de negócio centralizadas no backend  
- Estrutura escalável para futuras funcionalidades  
- Organização e clareza de código  
- Aprendizado prático de arquitetura full stack  

---

## 🧱 Arquitetura do Projeto

O projeto segue o modelo **Frontend + API REST**, com comunicação via **HTTP (JSON)**.

Frontend (React + Vite)
│
│ Requisições HTTP (Axios)
▼
Backend (FastAPI)
│
│ ORM (SQLAlchemy)
▼
Banco de Dados (PostgreSQL - Supabase)

shell
Copiar código

### Estrutura Geral do Repositório

Nova-Coworking/
├─ backend/
│ ├─ main.py
│ ├─ database.py
│ ├─ models/
│ ├─ schemas/
│ └─ router/
├─ frontend/
│ └─ nova-vite-project/
└─ README.md

yaml
Copiar código

---

## 🔧 Tecnologias Utilizadas

### Backend
- Python 3.11+
- FastAPI
- SQLAlchemy (ORM)
- Pydantic
- PostgreSQL (Supabase)
- Uvicorn
- CORS Middleware

### Frontend
- React
- Vite
- Axios
- React Router DOM
- CSS puro (`App.css`)

---

## 🎯 Objetivo do Sistema

- Cadastrar usuários administrativos  
- Cadastrar salas com capacidade e recursos  
- Criar, listar e excluir reservas  
- Evitar conflitos de horário entre reservas  
- Exibir agenda visual por dia  
- Fornecer visão geral no dashboard  

---

## 🔐 Regras de Negócio (Decisão Arquitetural)

- Toda regra de negócio fica no backend  
- O frontend não valida conflitos  
- O frontend apenas envia dados  
- O backend decide:
  - Se a reserva é válida  
  - Se há conflito de horário  
  - Se está dentro do horário permitido  

📌 O sistema inicia no **Dashboard**  
📌 Não existe página **Home**

---

## 🗄️ Backend

### 📂 Estrutura de Pastas

backend/
├─ main.py → Inicialização da aplicação
├─ database.py → Conexão com banco
├─ models/ → Modelos SQLAlchemy
│ ├─ usuarios.py
│ ├─ salas.py
│ └─ reservas.py
├─ schemas/ → Schemas Pydantic
│ ├─ usuario.py
│ ├─ sala.py
│ └─ reserva.py
└─ router/ → Rotas da API
├─ usuarios.py
├─ salas.py
└─ reservas.py

yaml
Copiar código

---

## 🧩 Entidades do Sistema

### 👤 Usuário
Campos:
- id  
- nome  
- email  
- senha (**NOT NULL**)  

#### ⚠️ Observação Importante sobre a Senha
Atualmente **não existe autenticação/login** no sistema.

O campo `senha` é obrigatório por **decisão arquitetural**, visando escala futura para:
- Login administrativo  
- Login de usuários finais  
- Separação de permissões (admin / usuário)  
- Implementação de JWT e controle de sessão  

📌 A senha **não é usada hoje**, mas o banco já está preparado para o futuro.

---

### 🏢 Sala
Campos:
- id  
- nome  
- capacidade  
- recursos  
- fotourl (opcional)  

---

### 📅 Reserva
Campos:
- id  
- usuario_id (FK)  
- sala_id (FK)  
- data_reserva (datetime)  
- duração (horas)  
- status  
- observacao  

---

## ⏰ Regras de Reserva (Backend)

- Horário permitido: **08:00 até 22:00**
- Duração mínima: **2 horas**
- Duração variável (definida pelo usuário)
- Não pode existir sobreposição de horários

A verificação de conflito compara:
- Início da nova reserva  
- Fim da nova reserva  
- Reservas existentes da mesma sala  

📌 Toda essa lógica fica **exclusivamente no backend**.

---

## 🔌 Endpoints da API

### Usuários
- GET `/usuarios`
- POST `/usuarios`
- PUT `/usuarios/{id}`
- DELETE `/usuarios/{id}`

### Salas
- GET `/salas`
- POST `/salas`
- PUT `/salas/{id}`
- DELETE `/salas/{id}`

### Reservas
- GET `/reservas`
- POST `/reservas`
- PUT `/reservas/{id}`
- DELETE `/reservas/{id}`
- GET `/reservas/sala/{sala_id}`
- GET `/reservas/usuario/{usuario_id}`

---

## 📑 Swagger (Documentação da API)

O backend utiliza **Swagger UI**, gerado automaticamente pelo FastAPI.

📍 Acesso:
http://127.0.0.1:8000/docs

yaml
Copiar código

No Swagger é possível:
- Ver todos os endpoints
- Testar requisições
- Visualizar schemas
- Simular POST, PUT e DELETE

---

## 🌐 CORS

Permite acesso apenas de:
- http://localhost:5173  
- http://127.0.0.1:5173  

---

## ▶️ Como Rodar o Backend

```bash
venv\Scripts\activate
uvicorn main:app --reload
API disponível em:

cpp
Copiar código
http://127.0.0.1:8000
🎨 Frontend
📂 Estrutura de Pastas
css
Copiar código
src/
├─ components/
│  ├─ Navbar.jsx
│  ├─ Card.jsx
│  └─ AgendaDia.jsx
├─ pages/
│  ├─ Dashboard.jsx
│  ├─ Usuarios.jsx
│  ├─ Salas.jsx
│  └─ Reservas.jsx
├─ services/
│  └─ api.js
├─ App.jsx
├─ App.css
└─ main.jsx
🧭 Navegação
Rota	Página
/	Dashboard
/usuarios	Usuários
/salas	Salas
/reservas	Reservas

📊 Dashboard
Cards informativos

Total de usuários

Total de salas

Total de reservas

Visão geral do sistema

👥 Usuários
CRUD funcional

Criação

Listagem

Exclusão

Senha obrigatória (uso futuro)

🏢 Salas
Listagem em grid

Limite visual de até 4 salas por linha

Exibição de capacidade e recursos

Botão para reservar

📅 Reservas
CRUD funcional

Seleção de usuário e sala

Escolha de data e duração

Exibição de:

horário inicial

horário final (calculado pela duração)

Agenda visual diária

🌐 Comunicação com Backend
Arquivo: src/services/api.js

js
Copiar código
import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000"
});

export default api;
▶️ Como Rodar o Frontend
bash
Copiar código
npm install
npm run dev
Aplicação disponível em:

arduino
Copiar código
http://localhost:5173
⚠️ Limitações Atuais
Sem autenticação

Sem permissões

Layout ainda em refinamento

Sem testes automatizados

Sem deploy em produção

🚀 Evoluções Planejadas
Autenticação JWT

Login público

Separação Admin / Usuário

Dashboard avançado

Testes automatizados

Docker

Deploy em nuvem

