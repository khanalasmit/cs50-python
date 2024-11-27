import pytest
from datetime import date
from seasons import Validation, main
from io import StringIO
import sys

# Test for the Validation class
def test_valid_date():
    valid_date = "2000-02-29"
    validation = Validation(valid_date)
    assert str(validation) == valid_date

def test_invalid_date_format():
    invalid_date = "02-29-2000"
    with pytest.raises(SystemExit):
        Validation(invalid_date)

def test_invalid_date_day():
    invalid_date = "2024-02-30"  # February 30th is invalid
    with pytest.raises(SystemExit):
        Validation(invalid_date)

def test_invalid_date_month():
    invalid_date = "2020-13-01"  # Month 13 doesn't exist
    with pytest.raises(SystemExit):
        Validation(invalid_date)

def test_non_digit_date():
    invalid_date = "2000-XX-XX"
    with pytest.raises(SystemExit):
        Validation(invalid_date)

# Test for minutes calculation in main logic
def test_leap_year_minutes():
    # February 29th, 2020, for a leap year calculation
    test_date = "2020-02-29"
    expected_output = "One million, fifty-two thousand, six hundred minutes"  # 1 year, 2 months, 29 days of minutes
    # Capture printed output
    captured_output = StringIO()
    sys.stdout = captured_output
    Validation(test_date)
    main()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip().capitalize() == expected_output

def test_non_leap_year_minutes():
    # January 1st, 2019 (non-leap year)
    test_date = "2019-01-01"
    expected_output = "Five hundred twenty-five thousand, six hundred minutes"  # 1 year, 1 day of minutes
    # Capture printed output
    captured_output = StringIO()
    sys.stdout = captured_output
    Validation(test_date)
    main()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip().capitalize() == expected_output

# Test for handling incorrect user input (invalid date format)
def test_invalid_input():
    with pytest.raises(SystemExit):
        captured_output = StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__

# Test for edge cases (for example, testing for year boundary)
def test_boundary_case():
    # January 1st, 2023
    test_date = "2023-01-01"
    expected_output = "Five hundred twenty-five thousand, six hundred minutes"  # Same as above since it's a normal year
    captured_output = StringIO()
    sys.stdout = captured_output
    Validation(test_date)
    main()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip().capitalize() == expected_output

