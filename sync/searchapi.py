import requests, os
import xml.etree.ElementTree as ET
from ygpt import generate_text_oai

FOLDER_ID = os.getenv('FOLDER_ID')
YANDEX_API_KEY = os.getenv('YANDEX_API_KEY')

QUERY = 'Что такое yandex gpt 4?'

url = 'https://yandex.ru/search/xml'
params = {
    'folderid': FOLDER_ID,
    'apikey': YANDEX_API_KEY,
    'query': QUERY,
    'lr': '11316',
    'l10n': 'ru',
    'sortby': 'rlv',
    'filter': 'strict',
    'groupby': 'attr=d.mode=deep.groups-on-page=5.docs-in-group=3',
    'maxpassages': '3',
    'page': '0'
}

response = requests.get(url, params=params)

#print(f"{response.text[:10]=}")

# Парсинг XML-ответа
root = ET.fromstring(response.text)

# Извлечение текстов из определенных тегов
passages = root.findall('.//passages')
passage_texts = []
for passage in passages:
    for text in passage.findall('passage'):
        passage_texts.append(text.text)
#print(passage_texts)

# Извлечение текстов из тега Snippet
snippets = root.findall('.//Snippet')
snippet_texts = []
for snippet in snippets:
    if snippet.text:
        snippet_texts.append(snippet.text)
#print(snippet_texts)

system = "Суммаризируй текст ниже"
user = "\n\n".join(snippet_texts)

gpt_answer = generate_text_oai(system, user, model='yandexgpt-32k/rc')
print(gpt_answer)
