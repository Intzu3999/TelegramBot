import googletrans
from googletrans import Translator

async def translate_text(text: str) -> str:
    translator = Translator()
    translation = translator.translate(text, src='en', dest='zh-cn')
    return translation.text
