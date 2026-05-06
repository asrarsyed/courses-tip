# Problem 1: Mountain Peak
def peak_index_in_mountain_list(lst: list[int]) -> int | None:
    for i in range(1, len(lst) - 1):
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            return i


mountain_lst = [0, 3, 8, 0]
peak = peak_index_in_mountain_list(mountain_lst)
print(peak)


# Problem 2: Build Inventory
def build_inventory(
    product_names: list[str], product_prices: list[float]
) -> dict[str, float]:
    d = {}
    for i in range(len(product_names)):
        d[product_names[i]] = product_prices[i]
    return d


product_names = ["Apple", "Banana", "Orange"]
product_prices = [0.99, 0.50, 0.75]
print(build_inventory(product_names, product_prices))


# Problem 3: Update or Warn
def update_or_warn(records: dict[str, int], item: str, update_value: int) -> None:
    if item in records:
        records[item] = update_value
    else:
        print(item + " not found!")


records = {"apple": 1, "banana": 2, "orange": 3}
update_or_warn(records, "grape", 4)
print(records)
update_or_warn(records, "banana", 5)
print(records)


# Problem 4: Attendance Rate
def attendance_rate(attendance_list: dict[str, str]) -> float:
    total = len(attendance_list)
    present = 0
    for v in attendance_list.values():
        if v == "Present":
            present += 1
    return (present / total) * 100


attendance_list = {
    "Bluey": "Present",
    "Bingo": "Absent",
    "Snickers": "Present",
    "Winton": "Absent",
}

print(attendance_rate(attendance_list))


# Problem 5: Average Book Ratings
def average_book_ratings(book_ratings: dict[str, list[float]]) -> dict[str, float]:
    result = {}
    for k, v in book_ratings.items():
        result[k] = sum(v) / len(v)
    return result


book_ratings = {
    "The Great Gatsby": [4.5, 3.0, 5.0],
    "To Kill a Mockingbird": [4.8, 5.0, 4.0, 4.9],
}

print(average_book_ratings(book_ratings))


# Problem 6: Odd Keys Even Values
def odd_keys_even_values(dictionary: dict[int, int]) -> list[int]:
    result = []
    for k, v in dictionary.items():
        if k % 2 != 0 and v % 2 == 0:
            result.append(k)
    return result


dictionary = {1: 2, 2: 6, 3: 5, 4: 4, 5: 8}
final_list = odd_keys_even_values(dictionary)
print(final_list)


# Problem 7: Best Team
def team_with_best_average_score(games: list[dict[str, int | str]]) -> str | None:
    totals = {}
    counts = {}
    for g in games:
        name = g["team_name"]
        score = g["score"]
        if name in totals:
            totals[name] += score
            counts[name] += 1
        else:
            totals[name] = score
            counts[name] = 1
    best_team = None
    best_avg = 0
    for name in totals:
        avg = totals[name] / counts[name]
        if avg > best_avg:
            best_avg = avg
            best_team = name
    return best_team


games = [
    {"team_name": "Lions", "score": 23},
    {"team_name": "Tigers", "score": 30},
    {"team_name": "Lions", "score": 27},
    {"team_name": "Bears", "score": 20},
    {"team_name": "Tigers", "score": 24},
    {"team_name": "Bears", "score": 22},
]

print(team_with_best_average_score(games))


# Problem 8: First Unique Items
def find_unique_items(list_a: list[str], list_b: list[str]) -> dict[str, bool]:
    result = {}
    for item in list_a:
        if item not in list_b:
            result[item] = True
    for item in list_b:
        if item not in list_a:
            result[item] = False
    return result


list_a = ["apple", "banana", "carrot"]
list_b = ["apple", "banana", "date"]
print(find_unique_items(list_a, list_b))
