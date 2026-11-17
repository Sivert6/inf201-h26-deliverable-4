
"""
Tests for the Fraction class. Run with: python -m pytest test_fraction.py -v

Sivert Svenningsen and Fabian Feiler, INF201 Deliverable 4
"""

import pytest

from fraction import Fraction


# Initialisation

def test_init() -> None:
    """Numerator and denominator are stored, and the default denominator is 1"""
    f = Fraction(3, 4)
    assert f.numerator == 3
    assert f.denominator == 4
    assert Fraction(5).denominator == 1


def test_init_reduces() -> None:
    """The fraction is reduced, e.g. 2/4 becomes 1/2"""
    f = Fraction(2, 4)
    assert f.numerator == 1
    assert f.denominator == 2


def test_init_zero() -> None:
    """Zero is stored as 0/1"""
    f = Fraction(0, 5)
    assert f.numerator == 0
    assert f.denominator == 1


@pytest.mark.parametrize("denominator", [0, -1, -5])
def test_init_invalid_denominator(denominator: int) -> None:
    """A denominator of 0 or below raises ValueError"""
    with pytest.raises(ValueError):
        Fraction(1, denominator)


@pytest.mark.parametrize("numerator, denominator", [(1.5, 2), (1, 2.0), ("1", 2)])
def test_init_not_integers(numerator: object, denominator: object) -> None:
    """Numerator and denominator that are not integers raise TypeError"""
    with pytest.raises(TypeError):
        Fraction(numerator, denominator)


# String representations

def test_repr() -> None:
    """repr() shows the fraction as code"""
    assert repr(Fraction(1, 2)) == "Fraction(1, 2)"


def test_str() -> None:
    """str() shows the fraction as text"""
    assert str(Fraction(-3, 4)) == "-3/4"


# Comparisons

def test_eq() -> None:
    """Equal fractions are equal even if written differently"""
    assert Fraction(1, 2) == Fraction(2, 4)
    assert not Fraction(1, 2) == Fraction(1, 3)


def test_ne() -> None:
    """Different fractions are not equal"""
    assert Fraction(1, 2) != Fraction(1, 3)
    assert not Fraction(1, 2) != Fraction(2, 4)


@pytest.mark.parametrize("small, large", [
    (Fraction(1, 3), Fraction(1, 2)),
    (Fraction(-1, 2), Fraction(1, 3)),
    (Fraction(2, 3), Fraction(3, 4)),
])
def test_ordering(small: Fraction, large: Fraction) -> None:
    """<, <=, > and >= give the correct answer"""
    assert small < large
    assert small <= large
    assert large > small
    assert large >= small
    assert not large < small
    assert not small > large


def test_le_ge_equal() -> None:
    """<= and >= are True for equal fractions"""
    assert Fraction(1, 2) <= Fraction(2, 4)
    assert Fraction(1, 2) >= Fraction(2, 4)


def test_compare_with_other_type() -> None:
    """Comparing with a non-Fraction gives NotImplemented"""
    assert Fraction(1, 2).__eq__(0.5) is NotImplemented
    assert Fraction(1, 2) != 0.5
    with pytest.raises(TypeError):
        Fraction(1, 2) < 1


# Arithmetic

@pytest.mark.parametrize("a, b, expected", [
    (Fraction(1, 2), Fraction(1, 3), Fraction(5, 6)),
    (Fraction(1, 4), Fraction(1, 4), Fraction(1, 2)),
    (Fraction(1, 2), Fraction(-1, 2), Fraction(0)),
])
def test_add(a: Fraction, b: Fraction, expected: Fraction) -> None:
    """a + b gives the correct reduced fraction"""
    assert a + b == expected


@pytest.mark.parametrize("a, b, expected", [
    (Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)),
    (Fraction(1, 2), Fraction(3, 4), Fraction(-1, 4)),
])
def test_sub(a: Fraction, b: Fraction, expected: Fraction) -> None:
    """a - b gives the correct reduced fraction"""
    assert a - b == expected


@pytest.mark.parametrize("a, b, expected", [
    (Fraction(2, 3), Fraction(3, 4), Fraction(1, 2)),
    (Fraction(-1, 2), Fraction(1, 3), Fraction(-1, 6)),
])
def test_mul(a: Fraction, b: Fraction, expected: Fraction) -> None:
    """a * b gives the correct reduced fraction"""
    assert a * b == expected


@pytest.mark.parametrize("a, b, expected", [
    (Fraction(1, 2), Fraction(1, 4), Fraction(2)),
    (Fraction(1, 2), Fraction(-1, 4), Fraction(-2)),
])
def test_truediv(a: Fraction, b: Fraction, expected: Fraction) -> None:
    """a / b gives the correct fraction, also when b is negative"""
    assert a / b == expected


def test_truediv_by_zero() -> None:
    """Dividing by a zero fraction raises ZeroDivisionError"""
    with pytest.raises(ZeroDivisionError):
        Fraction(1, 2) / Fraction(0)


def test_result_is_new_fraction() -> None:
    """Arithmetic returns a new Fraction and does not change the original"""
    a = Fraction(1, 2)
    result = a + Fraction(1, 3)
    assert isinstance(result, Fraction)
    assert a == Fraction(1, 2)
