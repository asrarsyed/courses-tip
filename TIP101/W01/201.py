# Problem 1: Print List
def print_list(lst: list[str]) -> None:
    for item in lst:
        print(item)


print_list(["squirtle", "gengar", "charizard", "pikachu"])


# Problem 2: Print Doubled List Items
def doubled(lst: list[int]) -> None:
    for item in lst:
        print(item * 2)


doubled([1, 2, 3])


# Problem 3: Return Doubled List
def doubledv2(lst: list[int]) -> list[int]:
    result = []
    for item in lst:
        result.append(item * 2)
    return result


lst = [1, 2, 3]
new_lst = doubledv2(lst)
print(new_lst)


# Problem 4: Flip Signs
def flip_sign(lst: list[int]) -> list[int]:
    result = []
    for item in lst:
        result.append(item * -1)
    return result


lst = [1, -2, -3, 4]
flipped_lst = flip_sign(lst)
print(flipped_lst)


# Problem 5: Max Difference
def max_difference(lst: list[int]) -> int:
    return max(lst) - min(lst)


lst = [5, 22, 8, 10, 2]
max_diff = max_difference(lst)
print(max_diff)


# Problem 6: Below Threshold
def count_less_than(numbers: list[int], threshold: int) -> int:
    count = 0
    for num in numbers:
        if num < threshold:
            count += 1
    return count


numbers = [12, 8, 2, 4, 4, 10]
counter = count_less_than(numbers, 5)
print(counter)


# Problem 7: Evens List
def get_evens(lst: list[int]) -> list[int]:
    result = []
    for item in lst:
        if item % 2 == 0:
            result.append(item)
    return result


lst = [1, 2, 3, 4]
evens_lst = get_evens(lst)
print(evens_lst)


# Problem 8: Multiples of Five
def multiples_of_five() -> None:
    for i in range(5, 101, 5):
        print(i)


multiples_of_five()


# Problem 9: Divisors
def find_divisors(n: int) -> list[int]:
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result


lst = find_divisors(6)
print(lst)


# Problem 10: FizzBuzz
def fizzbuzz(n: int) -> None:
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizzbuzz(13)


# Problem 11: Print the Index
def print_indices(lst: list[int]) -> None:
    for i in range(len(lst)):
        print(i)


lst = [5, 1, 3, 8, 2]
print_indices(lst)


# Problem 12: Linear Search
def linear_search(lst: list[int], target: int) -> int:
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


lst = [1, 4, 5, 2, 8]
position = linear_search(lst, 5)
print(position)

lst = [1, 4, 5, 2, 8]
position = linear_search(lst, 10)
print(position)
