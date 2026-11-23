# INF201 Deliverable 4

Sivert Svenningsen and Fabian Feiler

This repository contains our solution to Deliverable 4 in INF201 at NMBU: a `Temperature` class and a `Fraction` class, both tested with pytest.

## Files

| File | Content |
|---|---|
| `temperature.py` | Task 1: `Temperature` class supporting Celsius, Fahrenheit and Kelvin |
| `test_temperature.py` | 47 pytest tests for `Temperature` |
| `fraction.py` | Task 2: `Fraction` class with comparisons and arithmetic |
| `test_fraction.py` | 34 pytest tests for `Fraction` |
| `deliverable_04.ipynb` | Notebook with descriptions, examples, test output and discussion |
| `requirements.txt` | Packages in the virtual environment |

## Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the tests

From the repository root:

```
python -m pytest -v
```

All 81 tests should pass.