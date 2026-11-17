"""
Tests for the Temperature class.

Run from the repository root with:
python -m pytest -v test_temperature.py
"""

import pytest

from temperature import Temperature

# Reference points as [celsius, fahrenheit, kelvin]
REFERENCE_POINTS = [
    [-273.15, -459.67, 0.0],  # Absolute zero
    [-40.0, -40.0, 233.15],  # Celsius-Fahrenheit crossover
    [0.0, 32.0, 273.15],  # Freezing point of water
    [37.0, 98.6, 310.15],  # Human body temperature
    [100.0, 212.0, 373.15],  # Boiling point of water
]

TOL = 1e-9


# 1. Initialization

def test_default_unit() -> None:
    assert Temperature(25).unit == "C"


@pytest.mark.parametrize("unit, expected",
                         [["c", "C"],
                          ["f", "F"],
                          ["k", "K"],
                          ["K", "K"]
                          ])
def test_unit_is_case_insensitive(unit: str, expected: str) -> None:
    assert Temperature(10, unit).unit == expected


def test_value_is_read_only() -> None:
    temp = Temperature(25, "C")
    with pytest.raises(AttributeError):
        temp.value = 30


def test_unit_is_read_only() -> None:
    temp = Temperature(25, "C")
    with pytest.raises(AttributeError):
        temp.unit = "F"


# 2. Validation

@pytest.mark.parametrize("unit", ["X", "R", "celsius", ""])
def test_invalid_unit_raises(unit: str) -> None:
    with pytest.raises(ValueError):
        Temperature(10, unit)


@pytest.mark.parametrize("value, unit",
                         [[-273.16, "C"],
                          [-459.68, "F"],
                          [-0.01, "K"]
                          ])
def test_below_absolute_zero_raises(value: float, unit: str) -> None:
    with pytest.raises(ValueError):
        Temperature(value, unit)


def test_invalid_target_unit_raises() -> None:
    with pytest.raises(ValueError):
        Temperature(10, "C").convert_to("X")


# 3. Conversions

@pytest.mark.parametrize("c, f, k", REFERENCE_POINTS)
def test_conversion_from_celsius(c: float, f: float, k: float) -> None:
    temp = Temperature(c, "C")
    assert temp.to_celsius() == pytest.approx(c, abs=TOL)
    assert temp.to_fahrenheit() == pytest.approx(f, abs=TOL)
    assert temp.to_kelvin() == pytest.approx(k, abs=TOL)


@pytest.mark.parametrize("c, f, k", REFERENCE_POINTS)
def test_conversion_from_fahrenheit(c: float, f: float, k: float) -> None:
    temp = Temperature(f, "F")
    assert temp.to_celsius() == pytest.approx(c, abs=TOL)
    assert temp.to_fahrenheit() == pytest.approx(f, abs=TOL)
    assert temp.to_kelvin() == pytest.approx(k, abs=TOL)


@pytest.mark.parametrize("c, f, k", REFERENCE_POINTS)
def test_conversion_from_kelvin(c: float, f: float, k: float) -> None:
    temp = Temperature(k, "K")
    assert temp.to_celsius() == pytest.approx(c, abs=TOL)
    assert temp.to_fahrenheit() == pytest.approx(f, abs=TOL)
    assert temp.to_kelvin() == pytest.approx(k, abs=TOL)


def test_convert_to_returns_new_temperature() -> None:
    original = Temperature(100, "C")
    converted = original.convert_to("f")
    assert isinstance(converted, Temperature)
    assert converted.unit == "F"
    assert converted.value == pytest.approx(212.0, abs=TOL)
    assert original.unit == "C"  # The original is unchanged


# 4. Round-trip conversions

@pytest.mark.parametrize("c, f, k", REFERENCE_POINTS)
def test_round_trip_c_f_k_c(c: float, f: float, k: float) -> None:
    original = Temperature(c, "C")
    result = original.convert_to("F").convert_to("K").convert_to("C")
    assert result.unit == "C"
    assert result.value == pytest.approx(original.value, abs=TOL)
    assert result == original


# 5. Cross-unit comparisons

def test_equal_across_units() -> None:
    assert Temperature(0, "C") == Temperature(32, "F")
    assert Temperature(0, "C") == Temperature(273.15, "K")
    assert Temperature(37, "C") == Temperature(98.6, "F")


def test_not_equal_across_units() -> None:
    assert Temperature(0, "C") != Temperature(0, "F")
    assert Temperature(0, "K") != Temperature(0, "C")


def test_ordering_across_units() -> None:
    assert Temperature(0, "C") < Temperature(50, "F")
    assert Temperature(100, "C") > Temperature(200, "F")
    assert Temperature(300, "K") > Temperature(0, "C")


def test_ordering_with_equal_values() -> None:
    assert Temperature(0, "C") <= Temperature(32, "F")
    assert Temperature(0, "C") >= Temperature(32, "F")
    assert Temperature(0, "C") <= Temperature(300, "K")
    assert Temperature(212, "F") >= Temperature(373.15, "K")


def test_compare_with_non_temperature() -> None:
    temp = Temperature(0, "C")
    assert temp.__eq__(0) is NotImplemented
    assert temp.__lt__(0) is NotImplemented
    assert temp != 0
    with pytest.raises(TypeError):
        temp < 0


# 6. Formatting

@pytest.mark.parametrize("value, unit, expected",
                         [[25, "C", "Temperature(25.0, 'C')"],
                          [98.6, "f", "Temperature(98.6, 'F')"],
                          [0, "K", "Temperature(0.0, 'K')"]
                          ])
def test_repr(value: float, unit: str, expected: str) -> None:
    assert repr(Temperature(value, unit)) == expected


@pytest.mark.parametrize("value, unit, expected",
                         [[25, "C", "25.00 °C"],
                          [98.6, "F", "98.60 °F"],
                          [273.15, "K", "273.15 K"]
                          ])
def test_str(value: float, unit: str, expected: str) -> None:
    assert str(Temperature(value, unit)) == expected
