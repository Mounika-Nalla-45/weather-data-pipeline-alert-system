from src.weather_alert.functional import (
    calculate_average,
    extract_temperatures,
    filter_high_temperatures,
    temperature_messages,
)


def test_extract_temperatures():
    result = extract_temperatures([25, 30, 35])

    assert result == [25.0, 30.0, 35.0]


def test_filter_high_temperatures():
    result = filter_high_temperatures([25, 36, 30, 40])

    assert result == [36, 40]


def test_calculate_average():
    result = calculate_average([20, 30, 40])

    assert result == 30


def test_calculate_average_empty_list():
    result = calculate_average([])

    assert result == 0.0


def test_temperature_messages():
    result = list(temperature_messages([28, 38, 30, 40]))

    assert result == ["NORMAL", "HIGH", "NORMAL", "HIGH"]