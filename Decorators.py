# Функция декоратора
def decoratorDiv(func):

    def inner(*args, **kwargs):
        print('<div>')
        func(*args, **kwargs)
        print('</div>')

    return inner

# Функция с добавленным декоратором
@decoratorDiv # helloWorld = decorator(helloWorld)
def helloWorld(*args):
    print(f'hello world {args}')

# Вызов функции
helloWorld(1,123,'21321','sdf',True)