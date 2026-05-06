# Problem 1: Return Book
def return_book(title: str, library: dict[str, int]) -> dict[str, int]:
    if title in library:
        library[title] += 1
    else:
        library[title] = 1
    return library


library = {"The Hobbit": 2, "1984": 1, "The Great Gatsby": 4}

updated_lib = return_book("1984", library)
print(updated_lib)

updated_lib = return_book("The Giver", library)
print(updated_lib)


# Problem 2: Dictionary Difference
def dict_difference(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    result = {}
    for k in d1:
        if k not in d2 or d1[k] != d2[k]:
            result[k] = d1[k]
    return result


d1 = {"a": 1, "b": 2, "c": 3, "d": 4}
d2 = {"b": 2, "d": 1}
print(dict_difference(d2, d1))


# Problem 3: Take from Stock
def pop_stock(
    items: dict[str, int], item_name: str, quantity: int
) -> dict[str, int] | str:
    if item_name not in items:
        return "Item does not exist"
    if items[item_name] < quantity:
        return "Not enough stock"
    items[item_name] -= quantity
    return items


items = {"chocolate": 20, "candy": 5, "chips": 10}

resultA = pop_stock(items, "candy", 2)
resultB = pop_stock(items, "candy", 5)
resultC = pop_stock(items, "lollipops", 5)
resultD = pop_stock(items, "chocolate", 5)

print(resultA)
print(resultB)
print(resultC)
print(resultD)


# Problem 4: Group By Frequency
def group_by_frequency(lst: list[str]) -> dict[int, list[str]]:
    freq = {}
    for x in lst:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    result = {}
    for k, v in freq.items():
        if v in result:
            result[v].append(k)
        else:
            result[v] = [k]
    return result


lst = ["a", "b", "c", "d", "d", "c", "e", "e", "e"]
print(group_by_frequency(lst))


# Problem 5: No Duplicates Allowed
def remove_duplicates_from_front(nums: list[int]) -> list[int]:
    seen = set()
    result = []
    for n in reversed(nums):
        if n not in seen:
            result.append(n)
            seen.add(n)
    return list(reversed(result))


nums = [6, 5, 3, 5, 2, 8, 3]
print(remove_duplicates_from_front(nums))


# Problem 6: First Repeating Element
def find_min_index_of_repeating(nums: list[int]) -> int | None:
    seen = {}
    min_index = None

    for i, val in enumerate(nums):
        if val in seen:
            # update minimum index of repeating element
            min_index = seen[val] if min_index is None else min(min_index, seen[val])
        else:
            seen[val] = i

    return min_index


nums = [5, 6, 3, 4, 3, 6, 4]
nums2 = [5, 6, 3, 4]
nums3 = [5, 6, 2, 4, 3, 4, 3]
print(find_min_index_of_repeating(nums))
print(find_min_index_of_repeating(nums2))
print(find_min_index_of_repeating(nums3))


# Problem 7: Target Sum
def two_sum(nums: list[int], target: int) -> list[int] | None:
    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -= 1


nums = [2, 7, 11, 15]
q_1 = two_sum(nums, 9)
q_2 = two_sum(nums, 18)

nums2 = [3, 3]
q_3 = two_sum(nums2, 6)

print(q_1)
print(q_2)
print(q_3)
