# 📝 TaskUp

**TaskUp** é uma aplicação web para gerenciamento de tarefas simples (CRUD). A ideia é permitir que o(a) usuário(a) crie, visualize, atualize e delete tarefas de forma prática. Este projeto está sendo desenvolvido com foco educacional para aprendizado de **Flask** e **boas práticas de arquitetura backend**.

---

## ⚙️ Tecnologias Utilizadas

* [Python 3.12](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* \[SQLite (banco de dados)]
* [Flask-CORS](https://flask-cors.readthedocs.io/)
* [Pytest](https://docs.pytest.org/)

---

## 📂 Estrutura do Projeto

```
TaskUp/
└── taskup-backend/
    ├── app/
    │   ├── __init__.py
    │   ├── models/
    │   │   ├── __init__.py
    │   │   └── task.py
    │   ├── routes/
    │   │   ├── __init__.py
    │   │   └── task_routes.py
    │   ├── config/
    │   │   ├── __init__.py
    │   │   └── settings.py
    │   └── extensions.py
    ├── tests/
    │   ├── __init__.py
    │   └── test_tasks.py
    ├── run.py
    ├── requirements.txt
    └── pytest.ini

```

---


## ✅ Funcionalidades Implementadas

* [x] Criar tarefas
* [x] Listar todas as tarefas
* [x] Buscar tarefa por ID
* [x] Atualizar tarefa
* [x] Deletar tarefa
* [x] Testes unitários com Pytest
* [x] Organização do código com Blueprints e extensão `db`

---

## 🔜 Próximos Passos (Roadmap)

* [ ] Criar interface frontend com Angular
* [ ] Integração frontend-backend via HTTP
* [ ] Autenticação de usuário
* [ ] Deploy da aplicação (Render/Heroku)
* [ ] Melhorias nos testes (ex: testes de erro, autenticação)
* [ ] Documentação com Swagger ou Postman

---

## 📚 Aprendizados

> Este projeto está sendo construído com foco em aprendizado das melhores práticas de desenvolvimento backend em Python. A proposta é seguir uma arquitetura modular, utilizando design patterns como Factory e organização em camadas.

---

## 💡 Sobre o Projeto

Este repositório é parte de uma jornada de aprendizado com foco em **desenvolvimento web fullstack**, utilizando Python (Flask) no backend e futuramente Angular no frontend. Todos os commits, erros e descobertas estão sendo documentados em posts no [LinkedIn](https://linkedin.com/in/carolinefons).

---

## 📸 Prints e Insomnia (em breve)

Será adicionado em breve imagens de uso da API via Insomnia/Postman.

---

## 🧑‍💻 Autora

Feito por [Carol Fonseca](https://github.com/carolfons)
