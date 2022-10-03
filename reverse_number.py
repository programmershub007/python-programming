"""
Reserve a number without using str
"""


def anti_str_reverse(val: int) -> int:
    place_val = 0
    while val > 0:
        place_val = place_val * 10 + (val % 10)
        val //= 10
    return place_val
