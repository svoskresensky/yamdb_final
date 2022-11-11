## Описание.
Проект предоставляет возможности взаимодействия с проектом YaMDb через API.

Описание API в формате технического задания доступно на url "/redoc/"

## Установка.
Клонировать репозиторий, установить виртуальное окружение, выполнить миграции, запустить сервер.

## Примеры.
Зарегистривать пользователя и получить confirmation_code на email:
```
POST http://127.0.0.1:8000/api/v1/auth/signup/
Content-Type: application/json

{
    "username": "user1",
    "email": "user1@me.ru"
} 
```
Получить токен пользователя:
```
POST http://127.0.0.1:8000/api/v1/auth/token/
Content-Type: application/json

{
    "username": "user1",
    "confirmation_code": "7IwAK7A9_HvEivqlkBx-hDkPdrFI96AGPZ4gitGXbRw"
}
```
Получить список зарегистрированных пользователей от имени администратора:
```
GET http://127.0.0.1:8000/api/v1/users/
Authorization: Bearer xxxxxxx

```
Добавить пользователя от имени администратора:
```
POST http://127.0.0.1:8000/api/v1/users/
Authorization: Bearer xxxxx
Content-Type: application/json

{
    "username": "user2",
    "email": "user2@me.ru",
    "role": "user"
}
```
![yamdb workflow](https://github.com/svoskresensky/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

```
Project IP http://158.160.19.78/
```
