import pypinyin

async def get_pinyin(text: str) -> str:
    pinyin_list = pypinyin.lazy_pinyin(text)
    return ' '.join(pinyin_list)
