import asyncio

from .anomaly import SlidingWindowZScoreDetector
from .pipeline import WeatherPipeline
from .sensor import SimulatedWeatherSensor


async def main() -> None:

    sensor = SimulatedWeatherSensor(
        interval=0.3,
        anomaly_every=10
    )

    detector = SlidingWindowZScoreDetector(
        window_size=10,
        threshold=2.5
    )

    pipeline = WeatherPipeline(
        sensor=sensor,
        detector=detector
    )

    await pipeline.run(count=30)


if __name__ == "__main__":
    asyncio.run(main())