from datetime import UTC, datetime

from src.weather_alert.models import Alert, WeatherReading


def test_weather_reading():
    timestamp = datetime.now(UTC)

    reading = WeatherReading(
        timestamp=timestamp,
        temperature=28.5,
        humidity=65.0,
    )

    assert reading.temperature == 28.5
    assert reading.humidity == 65.0
    assert reading.timestamp == timestamp


def test_alert():
    timestamp = datetime.now(UTC)

    alert = Alert(
        timestamp=timestamp,
        message="Anomalous temperature detected",
        value=38.5,
        z_score=4.2,
    )

    assert alert.value == 38.5
    assert alert.z_score == 4.2
    assert alert.message == "Anomalous temperature detected"