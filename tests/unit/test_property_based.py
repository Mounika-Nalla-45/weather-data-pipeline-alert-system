from hypothesis import given
from hypothesis import strategies as st

from src.weather_alert.anomaly import mean, standard_deviation


@given(
    st.lists(
        st.floats(
            min_value=-50,
            max_value=50,
            allow_nan=False,
            allow_infinity=False,
        ),
        min_size=1,
        max_size=20,
    )
)
def test_mean_is_within_range(values):
    result = mean(values)

    minimum = min(values)
    maximum = max(values)

    assert minimum - 1e-12 <= result <= maximum + 1e-12

@given(
    st.lists(
        st.floats(
            min_value=-50,
            max_value=50,
            allow_nan=False,
            allow_infinity=False,
        ),
        min_size=1,
        max_size=20,
    )
)
def test_standard_deviation_is_non_negative(values):
    result = standard_deviation(values)

    assert result >= 0


@given(
    st.floats(
        min_value=-50,
        max_value=50,
        allow_nan=False,
        allow_infinity=False,
    )
)
def test_constant_values_have_zero_standard_deviation(value):
    values = [value, value, value]

    result = standard_deviation(values)

    assert abs(result) < 1e-12