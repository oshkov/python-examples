import psycopg2

# Параметры для подключения к БД
HOST = '127.0.0.1'
USER = 'postgres'
PASSWORD = '12345'
DB_NAME = 'pythonTest'

try:
    # Подключение к БД
    connection = psycopg2.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DB_NAME
    )

    # Автосохранение, чтобы каждый раз не писать connection.commit()
    connection.autocommit = True


    with connection.cursor() as cursor: # Создание курсора для БД
        cursor.execute(
            'SELECT version();'
        )
        print(f'Версия: {cursor.fetchone()}')


    # Создание таблицы
    with connection.cursor() as cursor:
        table_name = 'users'
        cursor.execute(
            f"""CREATE TABLE {table_name}(
                id serial PRIMARY KEY,
                first_name varchar(30) NOT NULL,
                second_name varchar(30) NOT NULL
            );"""
        )
        # connection.commit() # Не нужен если connection.autocommit = True
        print(f'Таблица {table_name} создана')


    # Создание записи в таблице
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO users (first_name, second_name) VALUES
            ('Oleg', 'Savchenko'),
            ('Alexander', 'Oshkov');"""
        )
        print('Пользователи добавлены')


    # Вывод значения из таблицы
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT second_name FROM users WHERE first_name = 'Oleg'"""
        )
        print(cursor.fetchone())


    # Вывод значения из таблицы
    with connection.cursor() as cursor:
        cursor.execute(
            f"""DROP TABLE {table_name}"""
        )
        print(f'Таблица {table_name} удалена')


except Exception as ex:
    print(f'ОШИБКА: {ex}')


finally:
    # Отключение от БД
    if connection:
        connection.close()
        print('БД отключена')