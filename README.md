# Weather Data Pipeline & Alert System

> **An end-to-end Python streaming pipeline that simulates weather sensor data, detects anomalous temperature readings using a sliding-window Z-score algorithm, raises alerts, validates the implementation with multiple testing strategies, evaluates performance, and packages the application with Docker.**

---

## 1. Project Overview

The **Weather Data Pipeline & Alert System** is a real-time-style data processing project developed in Python.

The system simulates a continuous stream of weather sensor readings containing:

- Temperature
- Humidity
- Timestamp

The incoming readings are processed immediately by an asynchronous pipeline. The system maintains a sliding window of recent temperature values and uses statistical anomaly detection to identify readings that are significantly different from the recent baseline.

When an anomalous temperature is detected, the system generates an alert containing:

- Alert timestamp
- Measured temperature
- Alert message
- Calculated Z-score

The project is designed as an engineering project rather than only a standalone Python program. It demonstrates:

- Streaming data ingestion
- Asynchronous programming
- Object-oriented programming
- Strategy Design Pattern
- Type hints and dataclasses
- Functional programming
- Sliding-window processing
- Statistical anomaly detection
- Unit testing
- Integration testing
- End-to-end testing
- Property-based testing
- Code coverage
- Static type checking
- Linting
- Performance benchmarking
- Docker containerisation
- Continuous Integration
- AI-assisted development with human validation

---

# 2. Real-World Problem

Weather monitoring systems continuously receive measurements from sensors.

A practical monitoring system should not only collect data but should also identify unusual values automatically.

For example:

```text
Normal temperatures:
27.2°C
28.1°C
27.8°C
29.0°C
28.4°C

Unexpected reading:
40.5°C
```

The system should be able to recognise that the latest value is unusual compared with recent observations.

### Problem Statement

> Design and implement a streaming weather data pipeline that continuously receives sensor readings and automatically detects anomalous temperature values using an efficient statistical method.

---

# 3. Project Objectives

The main objectives are:

1. Simulate continuous weather sensor data.
2. Process readings asynchronously.
3. Represent sensor data using structured Python models.
4. Maintain a sliding window of recent readings.
5. Calculate the mean and standard deviation.
6. Detect anomalous readings using the Z-score.
7. Generate alerts when the configured threshold is exceeded.
8. Separate anomaly detection from pipeline processing using the Strategy Pattern.
9. Demonstrate functional programming techniques.
10. Validate the system using multiple levels of testing.
11. Measure performance for different window sizes.
12. Run static analysis and linting.
13. Package the application using Docker.
14. Automate quality checks using CI.
15. Document the use and validation of AI-assisted development.

---

# 4. Key Features

| Feature | Implementation |
|---|---|
| Sensor data generation | `SimulatedWeatherSensor` |
| Streaming | Async generator |
| Data model | Python dataclasses |
| Processing | `WeatherPipeline` |
| Anomaly detection | Sliding-window Z-score |
| Detection abstraction | Strategy Pattern |
| Functional programming | `map`, `filter`, lambda, generator |
| Testing | Pytest |
| Property testing | Hypothesis |
| Coverage | Pytest-Cov |
| Type checking | Mypy |
| Linting | Ruff |
| Performance | Custom benchmark |
| Containerisation | Docker |
| CI | GitHub Actions |
| AI-assisted development | Documented and validated |

---

# 5. High-Level Architecture

```text
                    +----------------------+
                    | Simulated Weather    |
                    | Sensor               |
                    +----------+-----------+
                               |
                               | Async Stream
                               v
                    +----------------------+
                    | WeatherReading       |
                    | timestamp            |
                    | temperature          |
                    | humidity             |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Weather Pipeline     |
                    |                      |
                    | async for reading    |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Anomaly Strategy     |
                    | Interface            |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Sliding Window       |
                    | Z-Score Detector     |
                    +----------+-----------+
                               |
                    +----------+-----------+
                    |                      |
                  Normal                Anomaly
                    |                      |
                    v                      v
                 [OK]                 [ALERT]
```

---

# 6. End-to-End Data Flow

The complete execution flow is:

```text
Start Application
       |
       v
Create Sensor
       |
       v
Create Anomaly Detector
       |
       v
Create Weather Pipeline
       |
       v
Start Async Stream
       |
       v
Generate Weather Reading
       |
       v
Add/Compare With Sliding Window
       |
       v
Calculate Mean
       |
       v
Calculate Standard Deviation
       |
       v
Calculate Z-Score
       |
       v
Is |Z| > Threshold?
      / \
    NO   YES
    |      |
    v      v
  [OK]   Create Alert
           |
           v
        [ALERT]
           |
           v
      Next Reading
           |
           v
     Pipeline Complete
```

---

# 7. Project Structure

```text
weather-data-pipeline-alert-system/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── src/
│   └── weather_alert/
│       ├── __init__.py
│       ├── models.py
│       ├── sensor.py
│       ├── anomaly.py
│       ├── pipeline.py
│       ├── functional.py
│       └── main.py
│
├── tests/
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_anomaly.py
│   │   ├── test_models.py
│   │   ├── test_functional.py
│   │   └── test_property_based.py
│   │
│   ├── integration/
│   │   ├── __init__.py
│   │   └── test_pipeline_integration.py
│   │
│   └── e2e/
│       ├── __init__.py
│       └── test_application.py
│
├── performance/
│   └── benchmark.py
│
├── docs/
│   ├── ARCHITECTURE.md
│   └── AI_ASSISTED_DEVELOPMENT.md
│
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

# 8. Module Responsibilities

## `models.py`

Contains the application's data models.

### `WeatherReading`

Represents one sensor reading:

```text
WeatherReading
 ├── timestamp
 ├── temperature
 └── humidity
```

### `Alert`

Represents an anomaly:

```text
Alert
 ├── timestamp
 ├── message
 ├── value
 └── z_score
```

Python `dataclass` is used to keep these models simple and readable.

---

## `sensor.py`

Contains:

```text
SimulatedWeatherSensor
```

The sensor generates weather readings asynchronously.

Normal temperature:

```python
random.uniform(26, 30)
```

Every tenth reading receives an artificial increase:

```python
temperature += 12
```

This creates predictable abnormal events for demonstration and testing.

The sensor uses:

```python
async def stream(...)
```

and:

```python
yield WeatherReading(...)
```

Therefore, readings can be processed one at a time instead of building a large list in memory.

---

# 9. Asynchronous Data Ingestion

The sensor uses Python's `asyncio` framework.

The important operation is:

```python
await asyncio.sleep(self.interval)
```

This simulates the delay between sensor readings.

The pipeline consumes the stream using:

```python
async for reading in self.sensor.stream(count):
```

### Why asynchronous programming?

The project models a streaming/I/O-style workload.

Instead of blocking the entire application while waiting for the next sensor reading, asynchronous execution allows the application to yield control while waiting.

Conceptually:

```text
Sensor waiting
     |
     v
Control can be yielded
     |
     v
Next reading arrives
     |
     v
Process reading
```

---

# 10. Sliding Window Anomaly Detection

The project uses a sliding window of recent temperature values.

Configured example:

```text
Window size = 10
Threshold   = 2.5
```

The detector uses:

```python
deque(maxlen=window_size)
```

A `deque` automatically removes old values when the maximum size is reached.

Example:

```text
Before:
[27, 28, 29, 28, 27]

New reading:
40

Window moves:
[28, 29, 28, 27, 40]
```

The system therefore focuses on recent data instead of the entire historical dataset.

---

# 11. Initial Baseline

The detector requires at least three previous readings before calculating the initial anomaly score.

```text
Reading 1 -> baseline
Reading 2 -> baseline
Reading 3 -> baseline
Reading 4 -> first detection check
```

The window size is still 10.

This means:

> `window_size=10` defines the maximum number of recent values retained, while the initial three readings provide the minimum baseline required before detection begins.

As more readings arrive, the window grows until it contains the latest 10 values.

---

# 12. Z-Score Algorithm

The system uses the Z-score to measure how far the current reading is from the recent mean.

## Mean

```text
mean = sum(values) / number of values
```

Mathematically:

```text
μ = Σx / n
```

---

## Standard Deviation

The population standard deviation used by the implementation is:

```text
σ = √(Σ(x - μ)² / n)
```

---

## Z-Score

For a new temperature `x`:

```text
Z = (x - μ) / σ
```

The implementation raises an alert when:

```text
|Z| > 2.5
```

The threshold is configurable.

---

# 13. Example Detection

Suppose recent temperatures are:

```text
20, 21, 20, 21, 20
```

and the new reading is:

```text
50°C
```

The new value is far away from the recent baseline.

The detector calculates:

```text
Mean
  |
  v
Standard Deviation
  |
  v
Z-Score
  |
  v
Compare |Z| with 2.5
  |
  v
Anomaly
```

The output contains:

```text
[ALERT] Temperature: 50.00°C
        Anomalous temperature detected
        Z-score: ...
```

---

# 14. Important Statistical Edge Case

If all recent values are identical:

```text
20, 20, 20
```

then:

```text
standard deviation = 0
```

The implementation checks:

```python
if deviation == 0:
    return None
```

This prevents division by zero.

This case is also explicitly tested.

---

# 15. Object-Oriented Design

The project demonstrates several OOP concepts.

## Dataclasses

Used for:

```text
WeatherReading
Alert
```

## Abstraction

The anomaly detector defines:

```python
class AnomalyStrategy(ABC):
```

with:

```python
def check(...)
```

as an abstract method.

## Composition

`WeatherPipeline` receives the sensor and detector:

```python
WeatherPipeline(
    sensor=sensor,
    detector=detector
)
```

The pipeline therefore does not create these objects internally.

This makes the components easier to replace and test.

---

# 16. Strategy Design Pattern

The anomaly detection algorithm is separated from the pipeline through the Strategy Pattern.

```text
              AnomalyStrategy
                    |
          +---------+---------+
          |                   |
 SlidingWindowZScore     Future Strategy
    Detector
```

The pipeline depends on the strategy interface rather than a specific algorithm.

This makes it possible to add another detection strategy later without redesigning the pipeline.

Possible future strategies include:

```text
Moving Average Detector
IQR Detector
Isolation Forest
Machine Learning Detector
```

---

# 17. Functional Programming

The project also contains a functional programming module:

```text
src/weather_alert/functional.py
```

It demonstrates:

- Pure functions
- `map`
- `filter`
- Lambda expressions
- Generator expressions
- Iterable-based processing

Examples include:

```python
extract_temperatures(...)
```

```python
filter_high_temperatures(...)
```

```python
calculate_average(...)
```

```python
temperature_messages(...)
```

The generator:

```python
return (
    "HIGH" if temperature > 35 else "NORMAL"
    for temperature in temperatures
)
```

produces values lazily.

---

# 18. Testing Strategy

Testing is divided into three levels.

```text
                    Testing
                       |
        +--------------+--------------+
        |              |              |
       Unit       Integration        E2E
        |              |              |
 Individual       Components       Complete
 functions        together        application
```

## Unit Testing

Tests individual components such as:

- Mean calculation
- Standard deviation
- Anomaly detection
- Alert callback
- Dataclasses
- Functional functions

## Integration Testing

Checks that:

```text
Sensor
  +
Detector
  +
Pipeline
```

work together.

## End-to-End Testing

Runs the complete application flow.

---

# 19. Property-Based Testing

The project uses **Hypothesis** for property-based testing.

Instead of testing only:

```text
[10, 20, 30]
```

Hypothesis automatically generates many valid inputs.

Properties tested include:

### Mean

```text
minimum <= mean <= maximum
```

### Standard deviation

```text
standard deviation >= 0
```

### Constant values

```text
[20, 20, 20] -> standard deviation = 0
```

This helps expose edge cases that may not be obvious in manually selected examples.

---

# 20. Test Coverage

The project was validated with automated tests.

Initial test execution produced:

```text
9 tests passed
```

After adding property-based and functional tests, the project contains additional automated checks across:

- Unit tests
- Property-based tests
- Integration tests
- End-to-end tests

Coverage was measured using:

```bash
python -m pytest --cov=src --cov-report=term-missing
```

The earlier coverage measurement reached approximately:

```text
98% overall coverage
```

Coverage is treated as a quality measurement, not as proof that every possible behaviour is correct.

---

# 21. Code Quality

The project uses:

## Ruff

For linting:

```bash
ruff check .
```

Expected successful result:

```text
All checks passed!
```

## Mypy

For static type checking:

```bash
mypy src
```

The project uses strict type checking:

```toml
[tool.mypy]
strict = true
```

## Pytest

For automated testing:

```bash
python -m pytest
```

---

# 22. Performance Evaluation

A separate benchmark is included:

```text
performance/benchmark.py
```

It evaluates processing performance for:

```text
Window size = 5
Window size = 10
Window size = 20
Window size = 50
```

The benchmark processes:

```text
10,000 readings
```

and measures:

- Total execution time
- Time per reading
- Throughput

Run it with:

```bash
python -m performance.benchmark
```

Running it as a module is important because the benchmark imports the application package from `src`.

---

# 23. Algorithm Complexity

Let:

```text
W = sliding window size
```

The current detector converts the deque to a list and calculates statistics for the current window.

Therefore, approximately:

```text
Time per reading = O(W)
Space = O(W)
```

For a fixed window size of 10:

```text
W = 10
```

the practical work per reading remains bounded.

### Possible optimisation

A future version could maintain rolling:

```text
sum
sum of squares
```

to calculate the mean and variance more efficiently.

That could reduce the statistical update work toward:

```text
O(1) per reading
```

while still maintaining:

```text
O(W) space
```

for the window.

---

# 24. Docker Containerisation

The application is packaged using Docker.

Dockerfile:

```text
Python 3.12 slim image
        |
        v
Set /app as working directory
        |
        v
Copy requirements
        |
        v
Install dependencies
        |
        v
Copy source code
        |
        v
Set PYTHONPATH
        |
        v
Run application
```

## Build Image

```bash
docker build -t weather-alert-system .
```

## Run Container

```bash
docker run --rm weather-alert-system
```

Docker provides a reproducible environment separate from the local `.venv`.

---

# 25. Continuous Integration

The project uses GitHub Actions for automated CI.

The workflow performs:

```text
Git Push / Pull Request
          |
          v
Checkout Repository
          |
          v
Setup Python 3.12
          |
          v
Install Dependencies
          |
          +----------+
          |          |
          v          v
        Ruff       Mypy
          |          |
          +----+-----+
               |
               v
             Pytest
               |
               v
          Quality Check
```

The CI workflow checks:

```text
Ruff
Mypy
Pytest
```

This means code can be validated automatically when changes are pushed or submitted through a pull request.

---

# 26. AI-Assisted Development

AI tools were used as development assistance during the project.

Areas included:

- Project structure planning
- Python code suggestions
- Testing ideas
- Debugging
- Code explanations
- Documentation
- Review suggestions

The development process was:

```text
Requirement
    |
    v
Architecture
    |
    v
Implementation
    |
    v
AI Assistance
    |
    v
Human Review
    |
    v
Testing
    |
    v
Linting
    |
    v
Type Checking
    |
    v
Manual Validation
```

AI-generated suggestions were not accepted blindly.

The final implementation was validated using:

- Unit tests
- Integration tests
- End-to-end tests
- Property-based tests
- Ruff
- Mypy
- Manual execution

A practical example occurred during property-based testing, where generated floating-point values exposed the need for numerical tolerance when checking that standard deviation was effectively zero.

Detailed information is available in:

```text
docs/AI_ASSISTED_DEVELOPMENT.md
```

---

# 27. Installation

## Step 1: Clone the Repository

```bash
git clone <repository-url>
cd weather-data-pipeline-alert-system
```

## Step 2: Create Virtual Environment

Windows PowerShell:

```powershell
python -m venv .venv
```

Activate:

```powershell
.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Step 3: Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

# 28. Run the Application

From the project root:

```bash
python -m src.weather_alert.main
```

Example output:

```text
Starting Weather Data Pipeline...

[OK] Temperature: 27.34°C
[OK] Temperature: 28.11°C
[OK] Temperature: 26.92°C
[OK] Temperature: 29.03°C
...
[ALERT] Temperature: 38.24°C
        Anomalous temperature detected
        Z-score: ...

...
Pipeline completed.
```

The exact values change because normal sensor values are randomly generated.

Every tenth simulated reading receives an artificial temperature increase, making anomaly events visible during demonstration.

---

# 29. Run All Tests

```bash
python -m pytest
```

For coverage:

```bash
python -m pytest --cov=src --cov-report=term-missing
```

For an HTML coverage report:

```bash
python -m pytest --cov=src --cov-report=html
```

The generated report can be opened from:

```text
htmlcov/index.html
```

---

# 30. Run Quality Checks

Run Ruff:

```bash
ruff check .
```

Run Mypy:

```bash
mypy src
```

Run tests:

```bash
python -m pytest
```

Recommended final validation sequence:

```bash
ruff check .
mypy src
python -m pytest
```

---

# 31. Run Performance Benchmark

```bash
python -m performance.benchmark
```

The benchmark evaluates multiple sliding-window sizes and reports performance measurements.

The benchmark is separate from normal application execution so that the production-style pipeline remains simple.

---

# 32. Run With Docker

Build:

```bash
docker build -t weather-alert-system .
```

Run:

```bash
docker run --rm weather-alert-system
```

The local Python virtual environment does not need to be copied into the Docker image.

The Docker image installs the required packages inside the container.

---

# 33. Development Workflow

The project follows an engineering workflow:

```text
Understand Requirement
        |
        v
Decompose Problem
        |
        v
Design Architecture
        |
        v
Implement Small Modules
        |
        v
Add Tests
        |
        v
Run Application
        |
        v
Debug
        |
        v
Run Ruff
        |
        v
Run Mypy
        |
        v
Run Pytest
        |
        v
Run Performance Benchmark
        |
        v
Build Docker Image
        |
        v
Run CI
        |
        v
Commit / Push
```

---

# 34. Example Demonstration Flow

For a project defence or live demonstration, the system can be explained in this order:

### Step 1 — Show the Problem

```text
Continuous weather readings need automatic anomaly detection.
```

### Step 2 — Show the Sensor

```text
Sensor -> asynchronous weather readings
```

### Step 3 — Show the Pipeline

```text
Sensor -> Pipeline -> Detector
```

### Step 4 — Explain the Algorithm

```text
Recent values
     |
     v
Mean + Standard Deviation
     |
     v
Z-score
     |
     v
Threshold = 2.5
     |
     v
Normal / Anomaly
```

### Step 5 — Run the Application

```bash
python -m src.weather_alert.main
```

### Step 6 — Show an Alert

```text
[ALERT] Temperature: 38.xx°C
        Anomalous temperature detected
        Z-score: ...
```

### Step 7 — Show Testing

```bash
python -m pytest
```

### Step 8 — Show Code Quality

```bash
ruff check .
mypy src
```

### Step 9 — Show Performance

```bash
python -m performance.benchmark
```

### Step 10 — Show Docker

```bash
docker build -t weather-alert-system .
docker run --rm weather-alert-system
```

### Step 11 — Show CI

Open the GitHub Actions workflow and demonstrate the automated checks.

---

# 35. Design Decisions

## Why a simulated sensor?

A real weather API or physical sensor is not required to demonstrate the core streaming architecture.

The simulator provides:

- Continuous readings
- Reproducible application behaviour
- Controlled anomaly injection
- Easy local execution
- No external API dependency

---

## Why `asyncio`?

The application represents a streaming/I/O-style workload where readings arrive over time.

Async generators provide a natural way to consume one reading at a time.

---

## Why a sliding window?

Recent weather conditions are more relevant to immediate anomaly detection than the entire historical dataset.

A sliding window also limits memory usage.

---

## Why Z-score?

Z-score provides a simple statistical measure of how far a value is from the recent mean in units of standard deviation.

It is easy to explain, implement, test, and benchmark.

---

## Why the Strategy Pattern?

The pipeline should not depend directly on one anomaly detection algorithm.

The strategy abstraction allows future detectors to be introduced without changing the main pipeline.

---

## Why `deque`?

`deque(maxlen=W)` naturally represents a fixed-size sliding window.

Old values are automatically discarded when new values arrive.

---

## Why property-based testing?

Manually written examples cannot cover every possible numerical input.

Hypothesis generates many inputs automatically and checks general mathematical properties.

---

# 36. Limitations

The current project is an engineering demonstration and has several limitations.

### Simulated data

The sensor is simulated rather than connected to physical weather sensors.

### Simple statistical model

The detector uses a Z-score rather than a machine-learning anomaly model.

### Fixed threshold

The threshold is configured manually:

```text
2.5
```

A production system would normally tune this using historical data and operational requirements.

### Temperature only

The current anomaly detector focuses on temperature.

Humidity is included in the reading model but is not currently used by the Z-score detector.

### Benchmark scope

The benchmark measures the current Python implementation under the local benchmark conditions. It is not a complete production capacity test.

---

# 37. Future Enhancements

Possible future improvements include:

1. Connect to real weather APIs or IoT sensors.
2. Store readings in a database.
3. Add humidity anomaly detection.
4. Add multi-variable anomaly detection.
5. Add configurable thresholds.
6. Add a REST API.
7. Add a web dashboard.
8. Add persistent alert history.
9. Add email or notification alerts.
10. Add machine-learning anomaly detection.
11. Add rolling statistical calculations for improved performance.
12. Add cloud deployment.
13. Add monitoring and logging.
14. Add load testing.
15. Add authentication and access control.

---

# 38. Project Results

The implemented project demonstrates a complete software-engineering pipeline:

```text
Real-World Problem
       |
       v
Problem Decomposition
       |
       v
Algorithm Selection
       |
       v
Python Implementation
       |
       v
OOP + Strategy Pattern
       |
       v
Async Streaming
       |
       v
Functional Programming
       |
       v
Unit + Integration + E2E Testing
       |
       v
Property-Based Testing
       |
       v
Coverage
       |
       v
Ruff + Mypy
       |
       v
Performance Benchmark
       |
       v
Docker
       |
       v
Continuous Integration
       |
       v
AI-Assisted Development
       |
       v
Validated End-to-End Application
```

---

# 39. Project Defence Summary

### One-minute explanation

> “My project is a Weather Data Pipeline and Alert System. It simulates continuous weather sensor readings and processes them asynchronously. Each reading contains timestamp, temperature and humidity. The pipeline sends the temperature to a sliding-window anomaly detector. I use a Z-score to compare the current reading with recent values. If the absolute Z-score exceeds 2.5, the system generates an alert. I used a deque for the sliding window, dataclasses for the models, an abstract strategy interface and the Strategy Pattern for anomaly detection. I also implemented functional programming examples using map, filter and generators. The project is validated using unit, integration, end-to-end and property-based tests. Ruff and Mypy are used for code quality, a benchmark evaluates different window sizes, and Docker packages the application. GitHub Actions can automatically run the quality checks and tests.”

---

# 40. Repository Documentation

Additional technical documentation:

```text
docs/
├── ARCHITECTURE.md
└── AI_ASSISTED_DEVELOPMENT.md
```

### `ARCHITECTURE.md`

Contains the detailed architecture, data flow, algorithm, complexity, design patterns, testing architecture, Docker and CI structure.

### `AI_ASSISTED_DEVELOPMENT.md`

Documents how AI assistance was used and how generated suggestions were reviewed and validated.


# 41. Conclusion

The **Weather Data Pipeline & Alert System** combines Python programming, algorithms, statistics, software architecture, testing and engineering practices into one end-to-end project.

The project begins with simulated sensor data and finishes with a validated, containerised application.

The complete pipeline is:

```text
Weather Sensor
      ↓
Async Data Stream
      ↓
Weather Reading
      ↓
Sliding Window
      ↓
Mean + Standard Deviation
      ↓
Z-Score
      ↓
Threshold Comparison
      ↓
OK / ALERT
      ↓
Testing + Quality Checks
      ↓
Performance Evaluation
      ↓
Docker
      ↓
CI
```

This repository is intended to demonstrate not only that the application works, but also how it was **designed, implemented, tested, validated, measured and packaged as a complete software project**.

---

## Author

**Mounika Nalla**

M.Tech Computer Science and Engineering

---

## License

This project is developed as an academic/project implementation.
