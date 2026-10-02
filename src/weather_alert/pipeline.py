from .anomaly import AnomalyStrategy
from .sensor import SimulatedWeatherSensor


class WeatherPipeline:

    def __init__(
        self,
        sensor: SimulatedWeatherSensor,
        detector: AnomalyStrategy
    ):
        self.sensor = sensor
        self.detector = detector

    async def run(self, count: int = 30) -> None:

        print("\nStarting Weather Data Pipeline...\n")

        async for reading in self.sensor.stream(count):

            alert = self.detector.check(reading)

            if alert:

                print(
                    f"[ALERT] "
                    f"Temperature: {reading.temperature:.2f}°C"
                )

                print(
                    f"        {alert.message}"
                )

                print(
                    f"        Z-score: "
                    f"{alert.z_score:.2f}"
                )

            else:

                print(
                    f"[OK] "
                    f"Temperature: "
                    f"{reading.temperature:.2f}°C"
                )

        print("\nPipeline completed.")