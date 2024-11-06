import os
import requests
from dotenv import load_dotenv
import base64

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение API-ключа из переменной окружения
API_KEY = os.getenv('YANDEX_API_KEY')

# URL для отправки запроса
id = "sprki0etb2i39rplk3t3"
url = f"https://operation.api.cloud.yandex.net/operations/{id}"


# Заголовки запроса, включая API-ключ для аутентификации
headers = {
    "Authorization": f"Api-Key {API_KEY}"
}

# Отправка GET-запроса
response = requests.get(url, headers=headers)

# Проверка успешности запроса и вывод результата
if response.status_code == 200:
    result = response.json()
    if result['done'] == True:
        raw_data = result['response']['rawData']
        decoded_data = base64.b64decode(raw_data).decode('utf-8')
        print(decoded_data)
    else:
        print(result)
else:
    print(f"Ошибка: {response.status_code}, {response.text}")
