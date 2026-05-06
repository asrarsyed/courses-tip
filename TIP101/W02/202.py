# Problem 1: Update Score
def update_score(scores: dict[str, int], player: str, points: int) -> dict[str, int]:
    if player in scores:
        scores[player] += points
    else:
        scores[player] = points
    return scores


scores = {"Alice": 100, "Bob": 90}
update_score(scores, "Alice", 10)
print(scores)
update_score(scores, "Calvin", 20)
print(scores)
update_score(scores, "Calvin", 5)
print(scores)


# Problem 2: Dictionary Intersection
def dict_intersection(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    result = {}
    for k in d1:
        if k in d2 and d1[k] == d2[k]:
            result[k] = d1[k]
    return result


d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 2, "c": 4}
print(dict_intersection(d1, d2))


# Problem 3: Filter by Price
def remove_items_below_price(
    items: dict[str, float], price_threshold: float
) -> list[str] | None:
    removed = []
    keys = list(items.keys())
    for k in keys:
        if items[k] < price_threshold:
            removed.append(k)
            del items[k]
    if len(removed) == 0:
        return None
    return removed


items = {"apple": 1.99, "banana": 0.99, "cherry": 3.49, "date": 0.69}
removed_list = remove_items_below_price(items, 1.00)
print(removed_list)
removed_list_two = remove_items_below_price(items, 1.00)
print(removed_list_two)


# Problem 4: Find Odd Occurrences
def find_odd_occurrences(numbers: list[int]) -> list[int]:
    counts = {}
    for n in numbers:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1
    result = []
    for k, v in counts.items():
        if v % 2 != 0:
            result.append(k)
    return result


numbers = [1, 4, 2, 3, 2, 3, 3, 4, 4, 4]
odd_list = find_odd_occurrences(numbers)
print(odd_list)


# Problem 5: Find Mode
def find_mode(lst: list[int]) -> int:
    count = {}
    for elem in lst:
        count[elem] = count.get(elem, 0) + 1

    return max(count.values())


lst = [1, 2, 3, 2, 3, 3, 4, 4, 4, 4]
mode = find_mode(lst)
print(mode)


# Problem 6: How Many Smaller
def smaller_numbers_than_current(nums: list[int]) -> list[int]:
    sorted_nums = sorted(nums)

    rank = {}
    for i, num in enumerate(sorted_nums):  # iterating index and values
        if num not in rank:  # if the value is not in dictionary
            rank[num] = i  # add it to a dictionary with index as the value

    return [
        rank[num] for num in nums
    ]  # list comprehension to replace values of nums with their id value in rank


nums = [6, 1, 2, 2, 3]
print(smaller_numbers_than_current(nums))


# Problem 7: Good Pairs
def num_identical_pairs(nums: list[int]) -> int:
    freq = {}
    count = 0

    for num in nums:
        if num in freq:
            count += freq[num]  # all previous occurrences form pairs with this one
            freq[num] += 1
        else:
            freq[num] = 1

    return count


nums = [1, 2, 3, 1, 1, 3]
print(num_identical_pairs(nums))

nums = [1, 2, 3]
print(num_identical_pairs(nums))

nums = [1, 1, 1, 1]
print(num_identical_pairs(nums))
