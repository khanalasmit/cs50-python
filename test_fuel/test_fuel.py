import pytest
from fuel import convert, gauge

@pytest.mark.parametrize("fraction, expected_output", [
    ("3/4", 75),
    ("1/2", 50),
    ("1/4", 25),
    ("0/1", 0),
    ("1/1", 100),
    ("99/100", 99),
    ("1/100", 1)
])
def test_convert(fraction, expected_output):
    assert convert(fraction) == expected_output

@pytest.mark.parametrize("fraction", [
    "1/0", "a/b", "1/a", "a/1", "1.5/2", "4/3"
])
def test_convert_invalid(fraction):
    with pytest.raises((ValueError, ZeroDivisionError)):
        convert(fraction)

@pytest.mark.parametrize("percentage, expected_output", [
    (0, "E"),
    (1, "E"),
    (50, "50%"),
    (75, "75%"),
    (99, "F"),
    (100, "F")
])
def test_gauge(percentage, expected_output):
    assert gauge(percentage) == expected_output

if __name__ == "__main__":
    pytest.main()
