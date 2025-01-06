import pytest
from datetime import date
from seasons import AgeInMinutes

def test_valid_date():
    dob ="2000-01-01"
    age_calculator = AgeInMinutes(dob)
    assert isinstance(age_calculator.calculate_age_in_minutes(), str)
    assert "thirteen million" in str(age_calculator)
def test_invalid_date_format():
    dob = "01-01-2001"
    with pytest.raises(SystemExit) as e:
        AgeInMinutes(dob)
    assert e.type == SystemExit
    assert e.value.code == 1

def test_future_date():

    future_dob = date.today().strftime("%Y-%m-%d")  # Today's date
    age_calculator = AgeInMinutes(future_dob)
    assert "zero" in str(age_calculator)

def test_edge_case_newborn():

    dob = date.today().strftime("%Y-%m-%d")
    age_calculator = AgeInMinutes(dob)
    assert "zero" in str(age_calculator)
