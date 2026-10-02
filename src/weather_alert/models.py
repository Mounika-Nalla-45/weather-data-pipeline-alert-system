from dataclasses import dataclass
from datetime import datetime


@dataclass
class WeatherReading:
    timestamp: datetime
    temperature: float
    humidity: float


@dataclass
class Alert:
    timestamp: datetime
    message: str
    value: float
    z_score: float