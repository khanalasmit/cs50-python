import pytest
from datetime import date
from seasons import calculate_minutes, DateOfBirth


def test_valid_date():
    dob = DateOfBirth("2000-01-01")
    assert str(dob) == "2000-01-01"


def test_invalid_date_format():
    with pytest.raises(SystemExit):
        DateOfBirth("01-01-2000")


def test_invalid_date_logic():
    with pytest.raises(SystemExit):
        DateOfBirth("2000-02-30")


def test_calculate_minutes_non_leap():
    dob = DateOfBirth("1999-01-01")
    today = date(2000, 1, 1)
    assert calculate_minutes(dob) == 525600  # Non-leap year


def test_calculate_minutes_leap():
    dob = DateOfBirth("1996-01-01")
    today = date(2000, 1, 1)
    assert calculate_minutes(dob) == 2103840  # Includes leap years


def test_calculate_partial_year():
    dob = DateOfBirth("1998-06-20")
    today = date(2000, 1, 1)
    assert calculate_minutes(dob) == 806400


def test_edge_case_today():
    dob = DateOfBirth("2023-12-11")
    today = date(2023, 12, 11)
    assert calculate_minutes(dob) == 0  # Born today


def test_future_date():
    with pytest.raises(ValueError):
        dob = DateOfBirth("3000-01-01")
