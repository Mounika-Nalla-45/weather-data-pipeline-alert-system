import time
from datetime import UTC, datetime

from src.weather_alert.anomaly import SlidingWindowZScoreDetector
from src.weather_alert.models import WeatherReading


def create_reading(temperature: float) -> WeatherReading:
    return WeatherReading(
        timestamp=datetime.now(UTC),
        temperature=temperature,
        humidity=60.0,
    )


def run_benchmark(window_size: int, number_of_readings: int = 10000) -> None:
    detector = SlidingWindowZScoreDetector(
        window_size=window_size,
        threshold=2.5,
    )

    start_time = time.perf_counter()

    for i in range(number_of_readings):
        temperature = 28.0 + (i % 5)
        reading = create_reading(temperature)
        detector.check(reading)

    end_time = time.perf_counter()

    total_time = end_time - start_time
    time_per_reading = total_time / number_of_readings
    throughput = number_of_readings / total_time

    print(f"\nWindow size: {window_size}")
    print(f"Readings processed: {number_of_readings}")
    print(f"Total time: {total_time:.6f} seconds")
    print(f"Time per reading: {time_per_reading:.9f} seconds")
    print(f"Throughput: {throughput:.2f} readings/second")


def main() -> None:
    print("Weather Pipeline Performance Benchmark")

    for window_size in [5, 10, 20, 50]:
        run_benchmark(window_size)


if __name__ == "__main__":
    main()