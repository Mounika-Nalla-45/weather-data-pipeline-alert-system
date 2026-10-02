from abc import ABC, abstractmethod
from collections import deque
from collections.abc import Callable
from math import sqrt

from .models import Alert, WeatherReading


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def standard_deviation(values: list[float]) -> float:
    average = mean(values)

    variance = sum(
        (value - average) ** 2
        for value in values
    ) / len(values)

    return sqrt(variance)


class AnomalyStrategy(ABC):

    @abstractmethod
    def check(
        self,
        reading: WeatherReading
    ) -> Alert | None:
        pass


class SlidingWindowZScoreDetector(AnomalyStrategy):

    def __init__(
        self,
        window_size: int = 10,
        threshold: float = 2.5,
        alert_callback: Callable[[Alert], None] | None = None
    ):
        self.window: deque[float] = deque(maxlen=window_size)
        self.threshold = threshold
        self.alert_callback = alert_callback

    def check(
        self,
        reading: WeatherReading
    ) -> Alert | None:

        if len(self.window) < 3:
            self.window.append(reading.temperature)
            return None

        values = list(self.window)

        average = mean(values)
        deviation = standard_deviation(values)

        self.window.append(reading.temperature)

        if deviation == 0:
            return None

        z_score = (
            reading.temperature - average
        ) / deviation

        if abs(z_score) > self.threshold:

            alert = Alert(
                timestamp=reading.timestamp,
                message="Anomalous temperature detected",
                value=reading.temperature,
                z_score=z_score
            )

            if self.alert_callback:
                self.alert_callback(alert)

            return alert

        return None