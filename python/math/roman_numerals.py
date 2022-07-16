"""
functions for converting to and from roman numerals
"""


def int_to_roman(num: int) -> str:
    """convert integer to roman numeral"""
    num_map = (
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    )

    result = ""
    for arabic, roman in num_map:
        factor, num = divmod(num, arabic)
        result += roman * factor
    return result


def roman_to_int(roman):
    """convert roman numeral to integer"""
    num_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i, arabic in enumerate(roman):
        if i + 1 == len(roman) or num_map[arabic] >= num_map[roman[i + 1]]:
            result += num_map[arabic]
        else:
            result -= num_map[arabic]
    return result


def test():
    """run test cases"""
    for i in range(3500):
        assert roman_to_int(int_to_roman(i)) == i
    assert int_to_roman(3) == "III"
    assert int_to_roman(4) == "IV"
    assert roman_to_int("III") == 3
    assert roman_to_int("IV") == 4


if __name__ == "__main__":
    test()
