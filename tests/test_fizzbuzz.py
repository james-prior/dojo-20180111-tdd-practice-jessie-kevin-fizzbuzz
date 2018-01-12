import pytest

from fizzbuzz import fizzbuzz

number_to_expected_value = {
    1: 1,
    2: 2,
}
@pytest.mark.parametrize('number, expected_value', number_to_expected_value.items())
def test_known_number_returns_expected(number, expected_value):
        assert expected_value == fizzbuzz(number)
