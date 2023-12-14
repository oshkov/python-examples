from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename
import smtplib

login = 'email'
password = 'password'

# Функция отправки сообщения
def send_email(to_addr, subject, text, file=None):

    # Создание объекта сообщения
    message = MIMEMultipart()
    message['From'] = login         # От кого
    message['To'] = to_addr         # Кому
    message['Subject'] = subject    # Тема сообщения

    # Создания объекта текста для сообщения 
    text = MIMEText(text)

    # Добавление текста к сообщению
    message.attach(text)

    if file:
        # Открытие файла
        with open(file, "rb") as f:
            # Создание объекта файла для сообщения
            file = MIMEApplication(f.read(), Name=basename(file))

        # Добавления файла к сообщению
        message.attach(file)

    # Отправка сообщения
    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)    # Сервер яндекса
    server.ehlo(login)
    server.login(login, password)                       # Вход в почту
    server.auth_plain()
    server.send_message(message)                        # Отправка сообщения
    server.quit()                                       # Выход


try:
    # Отправка сообщения
    send_email(login, 'Тема', 'Текст')
    print('message successfuly sent')

except Exception as error:
    # Вывод ошибки
    print(f'ERROR: {error}')