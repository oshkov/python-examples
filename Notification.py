import time

NOTIFY_TIME = '13:27' # Время когда нужно отправить уведомление

while True:
    timeNow = time.strftime('%H:%M')
    print(f'{timeNow}: Проверка времени')

    if timeNow == NOTIFY_TIME:
        print("Уведомление отправлено")
        time.sleep(60) # Пауза на минуту, чтобы уведомление отправилось только один раз
    else:
        print('Уведомление НЕ отправлено')
        time.sleep(1)
