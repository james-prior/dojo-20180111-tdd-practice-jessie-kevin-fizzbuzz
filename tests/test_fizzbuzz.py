import pytest

from fizzbuzz import fizzbuzz

number_to_expected_value = {
    1: 1,
    2: 2,
    5: 'buzz',
    3: 'fizz',
    7: 7,
    15: 'fizzbuzz',
    23: 23,
    101: 101,
    102: 'fizz',
    20: 'buzz',
}
@pytest.mark.parametrize('number, expected_value', number_to_expected_value.items())
def test_known_number_returns_expected(number, expected_value):
        assert expected_value == fizzbuzz(number)
