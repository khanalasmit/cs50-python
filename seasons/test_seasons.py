from seasons import calculate_minutes, convert_to_words
from datetime import date

def test_calculate_minutes():
    # Test 1 year ago (non-leap year)
    birth_date = date(2023, 11, 27)
    assert calculate_minutes(birth_date) == 525600

    # Test 1 year ago (leap year)
    birth_date = date(2019, 11, 27)
    assert calculate_minutes(birth_date) == 527040

    # Test arbitrary date
    birth_date = date(2000, 1, 1)
    today = date(2024, 11, 27)
    delta = today - birth_date
    expected_minutes = round(delta.total_seconds() / 60)
    assert calculate_minutes(birth_date) == expected_minutes

def test_convert_to_words():
    assert convert_to_words(525600) == "five hundred twenty five thousand six hundred"
    assert convert_to_words(527040) == "five hundred twenty seven thousand forty"
    assert convert_to_words(1051200) == "one million fifty one thousand two hundred"
