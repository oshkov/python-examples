import threading
import time

# Функции
def first_func():
    print('Запуск первой функции')
    time.sleep(3)
    print('Завершение первой функции')

def second_func(a,b,c):
    print(f'Запуск второй функции, параметры: {a}, {b}, {c}')
    time.sleep(4)
    print(f'Завершение второй функции, параметры: {a}, {b}, {c}')


# Создаение переменных на основе классов потоков
first_func = threading.Thread(target=first_func)
second_func = threading.Thread(target=second_func, args=('4', 213, True))

# Запуск потоков, через переменные
first_func.start()
second_func.start()

# Вывод главного потока
print(threading.main_thread())

# Вывод количества потоков
print(threading.active_count())

# Вывод работающих потоков
print(threading.enumerate())
