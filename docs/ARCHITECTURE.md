# System Architecture

## Weather Data Pipeline & Alert System

This document describes the complete architecture, data flow, algorithms, software design, testing, performance evaluation, containerisation, and engineering practices implemented in the Weather Data Pipeline & Alert System.

---

# 1. Project Overview

The Weather Data Pipeline & Alert System is a Python-based streaming application that simulates weather sensor readings and detects anomalous temperature values.

The system continuously:

1. Generates weather readings.
2. Streams readings asynchronously.
3. Represents readings using structured data models.
4. Processes readings through a pipeline.
5. Maintains a sliding window of recent temperatures.
6. Calculates statistical values.
7. Computes a Z-score.
8. Detects anomalous readings.
9. Generates alerts.
10. Displays normal and anomalous readings.

The project also demonstrates:

- Object-Oriented Programming
- Strategy Design Pattern
- Functional Programming
- Asynchronous programming
- Unit testing
- Integration testing
- End-to-end testing
- Property-based testing
- Static type checking
- Code linting
- Performance benchmarking
- Docker containerisation
- AI-assisted development

---

# 2. Problem Statement

Weather monitoring systems receive continuous sensor readings.

A large stream of readings makes it difficult to manually identify unusual temperature values.

The system therefore needs to:

- continuously ingest readings,
- process them efficiently,
- maintain recent historical values,
- identify statistically unusual temperatures,
- generate alerts,
- and provide a reliable and testable software architecture.

---

# 3. High-Level Architecture

```text
                    +-----------------------+
                    | Simulated Weather     |
                    | Sensor                |
                    +-----------+-----------+
                                |
                                | Async WeatherReading
                                v
                    +-----------------------+
                    | Weather Pipeline      |
                    +-----------+-----------+
                                |
                                v
                    +-----------------------+
                    | Anomaly Strategy      |
                    | Sliding Window        |
                    | Z-Score Detector      |
                    +-----------+-----------+
                                |
                    +-----------+-----------+
                    |                       |
                    v                       v
              Normal Reading          Anomalous Reading
                    |                       |
                    v                       v
                 [OK]                   [ALERT]
```

---

# 4. Complete Project Structure

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

# 5. Source Code Architecture

## 5.1 models.py

`models.py` contains the core data structures.

Two dataclasses are used.

### WeatherReading

```text
WeatherReading
├── timestamp
├── temperature
└── humidity
```

### Alert

```text
Alert
├── timestamp
├── message
├── value
└── z_score
```

Dataclasses provide a simple and readable representation of structured data.

---

# 6. Sensor Layer

File:

```text
src/weather_alert/sensor.py
```

The `SimulatedWeatherSensor` class simulates a continuous weather sensor.

It generates:

- temperature
- humidity
- timestamp

Normal temperature values are generated in a specified range.

Every configured number of readings, the sensor adds an artificial temperature increase to simulate an anomalous reading.

The sensor uses asynchronous programming through an asynchronous generator and `asyncio.sleep()`.

---

# 7. Asynchronous Data Ingestion

The sensor produces readings through an asynchronous generator.

```text
Sensor
   |
   | async generator
   v
WeatherReading
   |
   v
Pipeline
```

The pipeline consumes readings using:

```python
async for reading in self.sensor.stream(count):
```

This allows the application to process streaming data asynchronously.

---

# 8. Processing Pipeline

File:

```text
src/weather_alert/pipeline.py
```

The `WeatherPipeline` class connects the sensor and anomaly detector.

Its responsibilities are:

1. Receive readings.
2. Pass each reading to the detector.
3. Check whether an alert was generated.
4. Display the result.

The pipeline uses composition:

```text
WeatherPipeline
├── Sensor
└── AnomalyStrategy
```

---

# 9. Anomaly Detection

File:

```text
src/weather_alert/anomaly.py
```

The project uses a Sliding Window Z-Score Detector.

The detector maintains recent temperature values using:

```python
deque(maxlen=window_size)
```

---

# 10. Sliding Window

For the current implementation:

```text
window_size = 10
```

The detector keeps at most the latest 10 values. When the window is full, older values are automatically removed.

---

# 11. Initial Baseline

The implementation begins anomaly checking after collecting a minimum of three readings.

The first three readings establish an initial statistical baseline.

From the fourth reading onward, the current temperature is compared with the previous readings.

```text
Minimum baseline = 3 readings
Maximum window   = configured window size
```

---

# 12. Mean Calculation

The arithmetic mean is:

```text
μ = Σx / n
```

where:

- μ = mean
- x = temperature value
- n = number of values

---

# 13. Standard Deviation

The detector calculates population standard deviation:

```text
σ = √( Σ(x - μ)² / n )
```

---

# 14. Z-Score

The current reading is converted into a Z-score:

```text
Z = (x - μ) / σ
```

The current threshold is:

```text
2.5
```

Decision:

```text
                Calculate Z-score
                       |
                       v
                |Z| > 2.5 ?
                  /                       Yes        No
                 |          |
                 v          v
              ALERT         OK
```

---

# 15. Zero Standard Deviation Handling

If all values in the window are identical, standard deviation can be zero.

The implementation avoids division by zero:

```python
if deviation == 0:
    return None
```

---

# 16. Strategy Design Pattern

The anomaly detector uses the Strategy Pattern.

The abstract interface is:

```python
class AnomalyStrategy(ABC):
    @abstractmethod
    def check(...):
        pass
```

The current concrete strategy is:

```text
SlidingWindowZScoreDetector
```

Architecture:

```text
             AnomalyStrategy
                    |
                    v
      SlidingWindowZScoreDetector
```

This allows another anomaly detection strategy to be added later without changing the pipeline.

---

# 17. Object-Oriented Design

The project demonstrates:

### Abstraction
`AnomalyStrategy` defines the detector interface.

### Composition
`WeatherPipeline` receives a sensor and detector.

### Encapsulation
Detector state such as the sliding window and threshold is maintained inside the detector object.

### Dataclasses
`WeatherReading` and `Alert` provide structured domain objects.

### Type Hints
Python type hints are used throughout the implementation.

---

# 18. Functional Programming

File:

```text
src/weather_alert/functional.py
```

Implemented functions include:

```text
extract_temperatures()
filter_high_temperatures()
calculate_average()
temperature_messages()
```

Functional techniques demonstrated:

- pure functions
- `map()`
- `filter()`
- lambda functions
- generator expressions
- reusable data transformations

---

# 19. Testing Architecture

Testing is divided into three main levels.

```text
                 Testing
                    |
       +------------+------------+
       |            |            |
       v            v            v
     Unit      Integration       E2E
```

## Unit Testing

Tests individual functions and classes, including anomaly calculations, data models, and functional utilities.

## Integration Testing

Tests interaction between:

```text
Sensor
   ↓
Pipeline
   ↓
Detector
```

## End-to-End Testing

Runs the complete application flow.

```text
Application
     ↓
Sensor
     ↓
Pipeline
     ↓
Detector
     ↓
Output
```

---

# 20. Property-Based Testing

The project uses Hypothesis for property-based testing.

Properties tested include:

- the mean remains within the range of input values,
- standard deviation is non-negative,
- identical values have approximately zero standard deviation.

This complements example-based testing by checking general properties across generated inputs.

---

# 21. Performance Evaluation

File:

```text
performance/benchmark.py
```

The benchmark processes:

```text
10,000 readings
```

and evaluates window sizes:

```text
5
10
20
50
```

It measures:

- total execution time
- time per reading
- throughput

Throughput is:

```text
Throughput = Number of readings / Total execution time
```

The benchmark provides practical performance measurements alongside theoretical complexity.

---

# 22. Algorithm Complexity

Let:

```text
W = sliding-window size
```

For each reading, the current implementation converts the window to a list and calculates the mean and standard deviation.

Therefore:

```text
Time complexity per reading = O(W)
Space complexity            = O(W)
```

---

# 23. Error and Edge-Case Handling

The implementation handles:

- insufficient initial readings
- zero standard deviation
- empty functional-programming input
- floating-point precision in property-based tests

---

# 24. Code Quality

### Ruff

```text
ruff check .
```

### Mypy

```text
mypy src
```

### Pytest

```text
python -m pytest
```

Project configuration is maintained in:

```text
pyproject.toml
```

---

# 25. Docker Architecture

The application is containerised using Docker.

```text
Dockerfile
     |
     v
Python 3.12 slim image
     |
     v
Install requirements
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

The container starts:

```text
python -m src.weather_alert.main
```

Docker provides an isolated and reproducible execution environment.

---

# 26. CI/CD Architecture

GitHub Actions is the continuous integration mechanism for the project.

The workflow performs:

```text
Git Push / Pull Request
          |
          v
    GitHub Actions
          |
     +----+----+----+
     |         |    |
     v         v    v
   Ruff      Mypy  Pytest
```

The workflow automatically checks:

- linting
- type checking
- automated tests

The current workflow is Continuous Integration; it does not perform production deployment.

---

# 27. AI-Assisted Development

AI tools were used as development assistance for:

- project structure
- implementation suggestions
- testing ideas
- debugging
- documentation
- code explanations

AI-generated suggestions were validated using:

- Unit tests
- Integration tests
- End-to-end tests
- Property-based tests
- Ruff
- Mypy
- manual execution

The process is documented separately in:

```text
docs/AI_ASSISTED_DEVELOPMENT.md
```

---

# 28. Complete End-to-End Flow

```text
                 WEATHER SENSOR
                       |
                       v
              Async Data Stream
                       |
                       v
                WeatherReading
                       |
                       v
              WEATHER PIPELINE
                       |
                       v
             Anomaly Strategy
                       |
                       v
             Sliding Window
                       |
                       v
             Mean + Std. Dev.
                       |
                       v
                  Z-Score
                       |
                 +-----+-----+
                 |           |
            |Z| > 2.5    |Z| <= 2.5
                 |           |
                 v           v
               ALERT         OK
                 |
                 v
          Display anomaly
```

---

# 29. Complete Engineering Workflow

```text
Problem Definition
       ↓
System Decomposition
       ↓
Architecture Design
       ↓
Python Implementation
       ↓
OOP + Strategy Pattern
       ↓
Async Data Ingestion
       ↓
Sliding Window Algorithm
       ↓
Z-Score Detection
       ↓
Functional Programming
       ↓
Unit Testing
       ↓
Integration Testing
       ↓
E2E Testing
       ↓
Property-Based Testing
       ↓
Static Type Checking
       ↓
Linting
       ↓
Performance Benchmark
       ↓
Docker Containerisation
       ↓
AI-Assisted Review
       ↓
Git + GitHub
       ↓
Continuous Integration
```

---

# 30. Final Architecture Summary

The Weather Data Pipeline & Alert System combines streaming data ingestion, statistical anomaly detection, object-oriented design, functional programming, automated testing, performance evaluation, containerisation, and engineering validation.

The core processing path is:

```text
Sensor
  ↓
Async Stream
  ↓
Pipeline
  ↓
Sliding Window
  ↓
Z-Score
  ↓
Threshold
  ↓
Alert / Normal
```

The project is modular so that the sensor, pipeline, data models, anomaly detection strategy, functional utilities, and testing components can be maintained and extended independently.
