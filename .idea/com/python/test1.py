import random
from typing import List, Any

def do_some_stuff():
    print("hello python")
    a = 1
    b: int = 8
    c = a + b
    print (c)

    nums = list(range(1,51))
    random.shuffle(nums)
    seven_nums: List[Any] = nums[:7]
    print(sorted(seven_nums))    # [1, 2, 7, 22, 25, 30, 42]

    # Python3 code to demonstrate working of
    # Summation of float string list
    # using sum() + float() + generator

    # initialize lists
    test_list = ['4.5', '7.8', '9.8', '10.3']

    # printing original list
    print("The original list is : " + str(test_list))

    # Summation of float string list
    # using sum() + float() + generator
    res_sum = sum(float(sub) for sub in test_list)

    # printing result
    print("The summation of float string list : " + str(res_sum))