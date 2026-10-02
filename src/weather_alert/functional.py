from collections.abc import Iterable


def extract_temperatures(readings: Iterable[float]) -> list[float]:
    """Return temperature values without modifying the input."""
    return list(map(lambda value: float(value), readings))


def filter_high_temperatures(
    temperatures: Iterable[float],
    limit: float = 35.0,
) -> list[float]:
    """Return temperatures above the given limit."""
    return list(filter(lambda value: value > limit, temperatures))


def calculate_average(temperatures: Iterable[float]) -> float:
    """Calculate the average temperature."""
    values = list(temperatures)

    if not values:
        return 0.0

    return sum(values) / len(values)


def temperature_messages(
    temperatures: Iterable[float],
) -> Iterable[str]:
    """Generate simple messages for temperatures."""
    return (
        "HIGH" if temperature > 35 else "NORMAL"
        for temperature in temperatures
    )