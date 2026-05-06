# Problem 1: Cast Vote
def cast_vote(votes: dict[str, int], candidate: str) -> dict[str, int]:
    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1
    return votes


votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)


# Problem 2: Keys in Common
def common_keys(dict1: dict[str, int], dict2: dict[str, int]) -> list[str]:
    result = []
    for k in dict1:
        if k in dict2:
            result.append(k)
    return result


dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)


# Problem 3: Frequency Count
def count_occurrences(nums: list[int]) -> dict[int, int]:
    d = {}
    for n in nums:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
    return d


nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums))


# Problem 4: Highest Priority Task
def get_highest_priority_task(tasks: dict[str, int]) -> str:
    highest = max(tasks, key=lambda k: tasks[k])
    tasks.pop(highest)
    return highest


tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = get_highest_priority_task(tasks)
print(perform_task)

perform_task = get_highest_priority_task(tasks)
print(perform_task)

perform_task = get_highest_priority_task(tasks)
print(perform_task)

print(tasks)


# Problem 5: Find Majority Element
def find_majority_element(elements: list[int]) -> int | None:
    count = {}
    for elem in elements:
        count[elem] = count.get(elem, 0) + 1
        if count[elem] > len(elements) // 2:
            return elem


elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))


# Problem 6: Has Duplicates
def has_duplicates(nums: list[int], k: int) -> bool:
    return False


"""
Understand:
- returns True if the list contains any duplicate elements within k (inclusive) indices of each other
- return True if nums[i] has the same value as any of the k neighboring elements to its left or right
- If k is greater than the list's length, the solution should check for duplicates in the complete list.
- The function should return False otherwise.

Match:
- sliding window + hash set

Plan:
-

Time Complexity:
Space Complexity:
"""

nums = [5, 6, 8, 2, 6, 4, 9]
check1 = has_duplicates(nums, 2)
print(check1)
check2 = has_duplicates(nums, 5)
print(check2)
check3 = has_duplicates(nums, 3)
print(check3)


# Problem 7: Make Pairs
def divide_list(nums: list[int]) -> bool:
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    return all(count % 2 == 0 for count in freq.values())


nums = [3, 2, 3, 2, 2, 2]
print(divide_list(nums))

nums = [1, 2, 3, 4]
print(divide_list(nums))
