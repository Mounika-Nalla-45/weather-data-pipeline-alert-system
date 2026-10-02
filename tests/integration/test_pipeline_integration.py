from src.weather_alert.anomaly import SlidingWindowZScoreDetector
from src.weather_alert.pipeline import WeatherPipeline
from src.weather_alert.sensor import SimulatedWeatherSensor


async def test_pipeline_integration():
    sensor = SimulatedWeatherSensor(
        interval=0.001,
        anomaly_every=5,
    )

    detector = SlidingWindowZScoreDetector(
        window_size=5,
        threshold=2.0,
    )

    pipeline = WeatherPipeline(
        sensor=sensor,
        detector=detector,
    )

    await pipeline.run(count=5)