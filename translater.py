import requests

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_me(text, api_key):
    params = {
        'key': api_key,
        'text': text,
        'lang': 'ru-sah'
    }
    response = requests.get(URL, params=params)
    json = response.json()
    return ''.join(json["text"])
