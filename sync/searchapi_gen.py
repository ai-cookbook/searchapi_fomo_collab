import requests
import os
from typing import Optional

def get_generative_search_response(
    query: str,
    folder_id: Optional[str] = None,
    api_key: Optional[str] = None
) -> dict:
    """
    Выполняет поисковый запрос с генеративным ответом через Yandex Search API
    """
    # Получаем креды из переменных окружения если не переданы
    folder_id = folder_id or os.getenv('FOLDER_ID')
    api_key = api_key or os.getenv('YANDEX_API_KEY')

    url = 'https://yandex.ru/search/xml/generative'
    data = {
        "messages": [
            {
                "content": "Сколько стоит Search API?",
                "role": "user"
            }
        ],
        "site": None,
        "host": None,
        "url": None
    }


    response = requests.post(url, json=data)
    response.raise_for_status()
    
    return response.json()

if __name__ == "__main__":
    QUERY = "Что такое нейронные сети?"
    
    try:
        result = get_generative_search_response(QUERY)
        # Получаем генеративный ответ из результата
        if 'message' in result and 'content' in result['message']:
            print(result['message']['content'])
        else:
            print("Генеративный ответ не получен")
            
    except Exception as e:
        print(f"Произошла ошибка: {e}")