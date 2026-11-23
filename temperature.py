"""
A Temperature class supporting Celsius, Fahrenheit and Kelvin.

Sivert Svenningsen and Fabian Feiler, INF201 Deliverable 4
"""

VALID_UNITS = ["C", "F", "K"]
TOLERANCE = 1e-9


class Temperature:
    """A temperature with a value and a unit (C, F or K)."""

    def __init__(self, value: float, unit: str = "C") -> None:
        """Create a temperature.

        Args:
            value: The temperature value.
            unit: "C", "F" or "K" (case-insensitive). Defaults to "C".

        Raises:
            ValueError: If the unit is invalid or the temperature is below absolute zero.
        """
        unit = unit.upper()
        if unit not in VALID_UNITS:
            raise ValueError(f"Invalid unit '{unit}'. Use 'C', 'F' or 'K'.")

        self._value = float(value)
        self._unit = unit

        if self.to_kelvin() < -TOLERANCE:
            raise ValueError("Temperature cannot be below absolute zero (0 K).")

    @property
    def value(self) -> float:
        """The temperature value (read-only)."""
        return self._value

    @property
    def unit(self) -> str:
        """The temperature unit (read-only)."""
        return self._unit

    def to_celsius(self) -> float:
        """Return the temperature in Celsius."""
        if self._unit == "K":
            return self._value - 273.15
        if self._unit == "F":
            return (self._value - 32) * 5 / 9
        return self._value

    def to_fahrenheit(self) -> float:
        """Return the temperature in Fahrenheit."""
        if self._unit == "C":
            return self._value * 9 / 5 + 32
        if self._unit == "K":
            return (self._value - 273.15) * 9 / 5 + 32
        return self._value

    def to_kelvin(self) -> float:
        """Return the temperature in Kelvin."""
        if self._unit == "C":
            return self._value + 273.15
        if self._unit == "F":
            return (self._value - 32) * 5 / 9 + 273.15
        return self._value

    def convert_to(self, target_unit: str) -> "Temperature":
        """Return a new Temperature converted to target_unit.

        Args:
            target_unit: "C", "F" or "K" (case-insensitive).

        Returns:
            A new Temperature object in the target unit.

        Raises:
            ValueError: If target_unit is invalid.
        """
        target_unit = target_unit.upper()
        if target_unit == "C":
            return Temperature(self.to_celsius(), "C")
        if target_unit == "F":
            return Temperature(self.to_fahrenheit(), "F")
        if target_unit == "K":
            return Temperature(self.to_kelvin(), "K")
        raise ValueError(f"Invalid unit '{target_unit}'. Use 'C', 'F' or 'K'.")

    def __repr__(self) -> str:
        return f"Temperature({self._value}, '{self._unit}')"

    def __str__(self) -> str:
        if self._unit == "K":
            return f"{self._value:.2f} K"
        return f"{self._value:.2f} °{self._unit}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return abs(self.to_kelvin() - other.to_kelvin()) < TOLERANCE

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return not self == other

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_kelvin() < other.to_kelvin() and not self == other

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return self < other or self == other

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_kelvin() > other.to_kelvin() and not self == other

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return self > other or self == other