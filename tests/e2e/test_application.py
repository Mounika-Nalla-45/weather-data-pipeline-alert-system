import pytest

from src.weather_alert.main import main


@pytest.mark.asyncio
async def test_complete_application():
    await main()