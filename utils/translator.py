import requests

def get_translation_from_api(text: str, api_key: str) -> dict:
    url = f"https://api.some-translation-service.com/translate?key={api_key}&text={text}&target_lang=zh"
    response = requests.get(url)
    return response.json()
