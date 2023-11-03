Платформа торговой сети электроники

Сеть должна представлять собой иерархическую структуру из 3 уровней:

Завод;
Розничная сеть;
Индивидуальный предприниматель.

Приложение retail_chain (торговая сеть):

Сеть (Link)
Контакты (Contacts)
Продукты (Products)

Стек технологий:
Python 3.8+
Django 3+
DRF 3.10+
PostgreSQL 10+

Для начала:
- необходимо создать из файла .env-sampel файл .env. 
- в PostgreSQL создать базу данных
- выполнить команду python manage.py migrate 



P.S:

Командой python manage.py create_superuser 
можно будет добавить учетная запись 2@admin.ru с паролем spartak67 
что бы войти в админку