from typing import List, Tuple
from random import randint, seed, shuffle
LARGE_NUMBERS = [25, 50, 75, 100]
SMALL_NUMBERS = list(range(1, 11)) * 2

def generate(n_large: int)->Tuple[List[int], int]:
    if n_large < 0 or n_large > 4:
        raise Exception("number of large numbers should be between 0 to 4")

    large_list = LARGE_NUMBERS.copy()
    small_list = SMALL_NUMBERS.copy()
    shuffle(large_list)
    shuffle(small_list)
    return sorted(large_list[:n_large] + small_list[:6 - n_large]), randint(100, 999)
