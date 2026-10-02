import asyncio
import random
from collections.abc import AsyncGenerator
from datetime import UTC, datetime

from .models import WeatherReading


class SimulatedWeatherSensor:

    def __init__(
        self,
        interval: float = 0.5,
        anomaly_every: int = 10
    ):
        self.interval = interval
        self.anomaly_every = anomaly_every

    async def stream(
        self,
        count: int = 30
    ) -> AsyncGenerator[WeatherReading, None]:

        for i in range(1, count + 1):

            await asyncio.sleep(self.interval)

            temperature = random.uniform(26, 30)
            humidity = random.uniform(55, 75)

            if i % self.anomaly_every == 0:
                temperature += 12

            yield WeatherReading(
                timestamp=datetime.now(UTC),
                temperature=temperature,
                humidity=humidity
            )