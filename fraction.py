
"""
Fraction class.

Sivert Svenningsen and Fabian Feiler, INF201 Deliverable 4
"""

from math import gcd


class Fraction:
    """Represents a fraction with an integer numerator and a positive denominator"""

    def __init__(self, numerator: int, denominator: int = 1) -> None:
        """
        Initialise the Fraction

        Args:
            numerator (int): The number above the line.
            denominator (int): The number below the line, must be > 0 (default = 1)
        """
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers")
        if denominator <= 0:
            raise ValueError("Denominator must be positive")

        divisor = gcd(numerator, denominator)  # Used to reduce the fraction, e.g. 2/4 -> 1/2
        self.numerator = numerator // divisor
        self.denominator = denominator // divisor

    def __repr__(self) -> str:
        """
        Return an unambiguous representation of the Fraction

        Returns:
            str: The fraction as code, e.g. Fraction(1, 2).
        """
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self) -> str:
        """
        Return a readable representation of the Fraction

        Returns:
            str: The fraction as text, e.g. 1/2.
        """
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other: object) -> bool:
        """
        Check if self == other

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if the fractions are equal.
        """
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other: object) -> bool:
        """
        Check if self != other

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if the fractions are not equal.
        """
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator != other.numerator * self.denominator

    def __lt__(self, other: object) -> bool:
        """
        Check if self < other

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if self is smaller than other.
        """
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other: object) -> bool:
        """
        Check if self <= other

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if self is smaller than or equal to other.
        """
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other: object) -> bool:
        """
        Check if self > other

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if self is greater than other.
        """
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other: object) -> bool:
        """
        Check if self >= other

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if self is greater than or equal to other.
        """
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __add__(self, other: "Fraction") -> "Fraction":
        """
        Add two fractions: a/b + c/d = (a*d + c*b) / (b*d)

        Args:
            other (Fraction): The fraction to add.

        Returns:
            Fraction: The sum as a new Fraction.
        """
        if not isinstance(other, Fraction):
            return NotImplemented
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other: "Fraction") -> "Fraction":
        """
        Subtract two fractions: a/b - c/d = (a*d - c*b) / (b*d)

        Args:
            other (Fraction): The fraction to subtract.

        Returns:
            Fraction: The difference as a new Fraction.
        """
        if not isinstance(other, Fraction):
            return NotImplemented
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other: "Fraction") -> "Fraction":
        """
        Multiply two fractions: a/b * c/d = (a*c) / (b*d)

        Args:
            other (Fraction): The fraction to multiply with.

        Returns:
            Fraction: The product as a new Fraction.
        """
        if not isinstance(other, Fraction):
            return NotImplemented
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        """
        Divide two fractions: a/b / c/d = (a*d) / (b*c)

        Args:
            other (Fraction): The fraction to divide by.

        Returns:
            Fraction: The quotient as a new Fraction.
        """
        if not isinstance(other, Fraction):
            return NotImplemented
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by a fraction equal to zero")

        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        if denominator < 0:  # Move the minus sign up, since the denominator must be positive
            numerator = -numerator
            denominator = -denominator
        return Fraction(numerator, denominator)




