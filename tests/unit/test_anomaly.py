from datetime import UTC, datetime

from src.weather_alert.anomaly import (
    SlidingWindowZScoreDetector,
    mean,
    standard_deviation,
)
from src.weather_alert.models import WeatherReading


def create_reading(temperature: float) -> WeatherReading:
    return WeatherReading(
        timestamp=datetime.now(UTC),
        temperature=temperature,
        humidity=60,
    )


def test_mean():
    assert mean([10, 20, 30]) == 20


def test_standard_deviation():
    result = standard_deviation([10, 20, 30])
    assert round(result, 2) == 8.16


def test_detector_creates_alert():
    detector = SlidingWindowZScoreDetector(
        window_size=5,
        threshold=2.0,
    )

    for temperature in [20, 21, 20, 21, 20]:
        detector.check(create_reading(temperature))

    anomaly = create_reading(50)

    result = detector.check(anomaly)

    assert result is not None


def test_detector_handles_zero_standard_deviation():
    detector = SlidingWindowZScoreDetector(
        window_size=5,
        threshold=2.0,
    )

    for temperature in [20, 20, 20]:
        detector.check(create_reading(temperature))

    result = detector.check(create_reading(20))

    assert result is None


def test_detector_calls_alert_callback():
    alerts = []

    detector = SlidingWindowZScoreDetector(
        window_size=5,
        threshold=2.0,
        alert_callback=alerts.append,
    )

    for temperature in [20, 21, 20, 21, 20]:
        detector.check(create_reading(temperature))

    result = detector.check(create_reading(50))

    assert result is not None
    assert len(alerts) == 1
    assert alerts[0] == result