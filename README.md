# KanBan - API Backend

Este é o back-end de uma aplicação de gerenciamento de tarefas estilo Kanban, desenvolvido com **Django** e **Django Rest Framework (DRF)**. Ele fornece uma API RESTful para gerenciar usuários, kanbans e tarefas.

## Funcionalidades da API

- **Autenticação de Usuários**: Registre e autentique usuários utilizando e-mail e senha.
- **Kanban**: Criação, leitura, atualização e exclusão de kanbans (quadros de tarefas).
- **Tarefas**: Criação, leitura, atualização e exclusão de tarefas dentro dos kanbans.
- **Controle de Acesso**: Cada usuário tem acesso apenas aos seus próprios kanbans e tarefas.

## Tecnologias Utilizadas

- **Django**: Framework Python para construção do back-end.
- **Django Rest Framework (DRF)**: Biblioteca para criar APIs RESTful de maneira rápida e eficiente.
- **SQLite**: Banco de dados simples (por padrão no Django) para armazenar os dados, mas pode ser facilmente configurado para outros bancos, como PostgreSQL.

***Exemplo de request utilizando [rest client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client):***

  ```bash
  ### Variables 
  @apiurl = http://127.0.0.1:8000
  
  
  # List Users
  GET {{apiurl}}/api/accounts/ HTTP/1.1
  Content-Type: application/json
  Authorization: Bearer <TOKEN>
  
  
  # login User
  POST {{apiurl}}/api/accounts/token/ HTTP/1.1
  Content-Type: application/json
  
  {
      "email": "sgsartur@hotmail.com",
      "password": "123456"
  }
  
  
  ### Create User
  POST {{apiurl}}/api/accounts/register/ HTTP/1.1
  Content-Type: application/json
  
  {
      "email": "sgsartur@hotmail.com",
      "password": "123456",
      "confirm_password": "123456"
  }

  ### Create Todo
  POST http://127.0.0.1:8000/api/todos/
  Authorization: Bearer <your_jwt_token>
  Content-Type: application/json

  {
    "name": "My New ToDo",
    "user": <user_id>
  }

  ### Create Column
  POST http://127.0.0.1:8000/api/columns/
  Authorization: Bearer <your_jwt_token>
  Content-Type: application/json

  {
    "name": "To Do",
    "todo": <todo_id>
  }

  ### Create Task
  POST http://127.0.0.1:8000/api/tasks/
  Authorization: Bearer <your_jwt_token>
  Content-Type: application/json

  {
    "title": "New Task",
    "description": "Task description",
    "column": <column_id>
  }


  ### Change Task Position
  PATCH {{apiurl}}/api/tasks/<task_id>/change_task_position/
  Authorization: Bearer <your_jwt_token>
  Content-Type: application/json

  {
    "position": 2
  }
  ```
