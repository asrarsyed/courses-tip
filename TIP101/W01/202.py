# Problem 1: Convert Temperature
def convertTemp(celsius: float) -> list[float]:
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32.00
    return [kelvin, fahrenheit]


temperatures = convertTemp(23.00)
print(temperatures)


# Problem 2: Average Score
def average(scores: list[int]) -> float:
    return sum(scores) / len(scores)


scores = [84, 73, 92, 95, 88]
avg_score = average(scores)
print(avg_score)


# Problem 3: Increment by 1
def increment_values(lst: list[int]) -> list[int]:
    result = []
    for num in lst:
        result.append(num + 1)
    return result


lst = [3, 5, 8, 2]
new_lst = increment_values(lst)
print(new_lst)


# Problem 4: Check for Number
def check_num(lst: list[int], num: int) -> bool:
    return num in lst


lst = [5, 2, 3, 9, 10]
flag1 = check_num(lst, 9)
flag2 = check_num(lst, 4)
print(flag1)
print(flag2)


# Problem 5: Missing Number
def find_missing(nums: list[int]) -> int:
    n = len(nums)
    return (n * (n + 1)) // 2 - sum(nums)


nums = [2, 4, 1, 0, 5]
missing_num = find_missing(nums)
print(missing_num)


# Problem 6: Reverse List
def reverse_list(lst: list[int]) -> list[int]:
    return lst[::-1]


lst = [1, 2, 3, 4, 5]
rev_lst = reverse_list(lst)
print(rev_lst)


# Problem 7: Get Odd Numbers
def get_odds(nums: list[int]) -> list[int]:
    result = []
    for num in nums:
        if num % 2 != 0:
            result.append(num)
    return result


nums = [2, 5, 1, 8, 6, 5]
odd_nums = get_odds(nums)
print(odd_nums)


# Problem 8: Multiplication Table
def multiplication_table(num: int) -> None:
    for i in range(1, 11):
        print(num * i)


multiplication_table(7)


# Problem 9: Create Number
def list_to_number(digits: list[int]) -> int:
    num = 0
    for d in digits:
        num = num * 10 + d
    return num


digits = [1, 0, 3]
number = list_to_number(digits)
print(number)


# Problem 10): Move Zeroes
def move_zeroes(nums: list[int]) -> list[int]:
    result = []
    zero_count = 0
    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            result.append(num)
    result.extend([0] * zero_count)
    return result


nums = [1, 0, 2, 3, 0, 0, 4]
new_nums = move_zeroes(nums)
print(new_nums)


# Problem 11: Odd Indices
def print_odd_indices(nums: list[int]) -> None:
    for i in range(len(nums)):
        if i % 2 == 1:
            print(nums[i])


nums = [3, 4, 8, 1, 5, 2]
print_odd_indices(nums)


# Problem 12: List Occurrences
def find_all_occurrences(lst: list[int], target: int) -> list[int]:
    result = []
    for i in range(len(lst)):
        if lst[i] == target:
            result.append(i)
    return result


lst = [1, 2, 6, 5, 2, 1, 3, 2, 2]
index_list = find_all_occurrences(lst, 2)
print(index_list)
