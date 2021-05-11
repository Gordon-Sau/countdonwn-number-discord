from typing import List, Union
from Int import Int
SEPARATOROR_LIST = ['+', '-', '*', '/', '(', ')', ' ', ]

def valid_expression(exp:str)->None:
    AVAILABLE_LIST = SEPARATOROR_LIST + [str(i) for i in range(10)]
    if "**" in exp:
        raise ValueError("you cannot type **")
    if "//" in exp :
        raise ValueError("you cannot type //")
    if not all(map(lambda x: x in AVAILABLE_LIST, exp)):
        raise ValueError("invalid expression")

def get_all_num_literals(exp: str)->List[str]:
    for separator in SEPARATOROR_LIST:
        exp = exp.replace(separator, ' ')
    return [num for num in exp.split()]

def valid_nums(input_list:List[int], usable_list: List[int])->None:
    usable_list = usable_list.copy()
    for num in input_list:
        if num in usable_list:
            usable_list.remove(num)
        else:
            raise ValueError(f"invalid number or repeated number: {num}")

def evaluate(exp:str, usable_list:List[int], target:int)->int:
    valid_expression(exp)
    nums = get_all_num_literals(exp)
    valid_nums([int(num) for num in nums], usable_list)
    ans = _evaluate(exp, nums)
    diff = abs(ans - target)
    if diff == 0:
        return 10
    elif diff <= 5:
        return 7
    elif diff <= 10:
        return 5
    else:
        return 0

def _evaluate(exp: str, nums: List[str])->int:
    Int_nums = [Int(num) for num in nums]
    for i, num in enumerate(nums):
        exp = exp.replace(num, f'Int_nums[{i}]', 1)
    return int(eval(exp))
