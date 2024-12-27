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
