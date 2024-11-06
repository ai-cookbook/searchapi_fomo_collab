import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение API-ключа из переменной окружения
API_KEY = os.getenv('YANDEX_API_KEY')

# URL для отправки запроса
url = "https://searchapi.api.cloud.yandex.net/v2/web/searchAsync"

# Параметры запроса
params = {
    "query": {
      "searchType": "SEARCH_TYPE_RU",
      "queryText": "yandex cloud foundational models",
      "familyMode": "FAMILY_MODE_NONE",
      "page": "1"
    },
    "sortSpec": {
      "sortMode": "<правило_сортировки_результатов>",
      "sortOrder": "<порядок_сортировки_результатов>"
    },
    "groupSpec": {
      "groupMode": "<метод_группировки_результатов>",
      "groupsOnPage": "<количество_групп_на_странице>",
      "docsInGroup": "<количество_документов_в_группе>"
    },
    "maxPassages": "<максимальное_количество_пассажей>",
    "region": "<идентификатор_региона>",
    "l10N": "<язык_уведомлений>",
    "folderId": "<идентификатор_каталога>"
}

# Параметры запроса
params = {
    "query": {
      "searchType": "SEARCH_TYPE_RU",
      "queryText": "yandex cloud foundational models",
      "familyMode": "FAMILY_MODE_NONE",
      "page": "1"
    },
    "folderId": os.getenv('FOLDER_ID')
}

# Заголовки запроса, включая API-ключ для аутентификации
headers = {
    "Authorization": f"Api-Key {API_KEY}"
}

# Отправка GET-запроса
response = requests.post(url, headers=headers, json=params)

# Проверка успешности запроса и вывод результата
if response.status_code == 200:
    print(response.json())
else:
    print(f"Ошибка: {response.status_code}, {response.text}")
