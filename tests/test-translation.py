import pytest
from bot.translation import translate_text

@pytest.mark.asyncio
async def test_translation():
    result = await translate_text("Hello")
    assert result == "你好"  # This would depend on the actual translation result
