# Problem 1: All In
def all_in(a: list[int], b: list[int]) -> bool:
    for x in a:
        if x not in b:
            return False
    return True


lst_1 = [1, 2]
lst_2 = [1, 2, 3]
print(all_in(lst_1, lst_2))
print(all_in(lst_2, lst_1))


# Problem 2: Create a Dictionary
def create_dictionary(keys: list[str], values: list[str]) -> dict[str, str]:
    d = {}
    for i in range(len(keys)):
        d[keys[i]] = values[i]
    return d


keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
print(create_dictionary(keys, values))


# Problem 3: Print Pair
def print_pair(dictionary: dict[str, str], target: str) -> None:
    if target in dictionary:
        print("Key:", target)
        print("Value:", dictionary[target])
    else:
        print("That pair does not exist!")


dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")


# Problem 4: Keys Versus Values
def keys_v_values(dictionary: dict[int, int]) -> str:
    key_sum = 0
    value_sum = 0
    for k, v in dictionary.items():
        key_sum += k
        value_sum += v
    if key_sum > value_sum:
        return "keys"
    elif value_sum > key_sum:
        return "values"
    else:
        return "balanced"


dictionary1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100: 10, 200: 20, 300: 30, 400: 40, 500: 50, 600: 60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)


# Problem 5: Restock Inventory
def restock_inventory(
    current_inventory: dict[str, int], restock_list: dict[str, int]
) -> dict[str, int]:
    for item, qty in restock_list.items():
        if item in current_inventory:
            current_inventory[item] += qty
        else:
            current_inventory[item] = qty
    return current_inventory


current_inventory = {"apples": 30, "bananas": 15, "oranges": 10}

restock_list = {"oranges": 20, "apples": 10, "pears": 5}

print(restock_inventory(current_inventory, restock_list))


# Problem 6: Calculate GPA
def calculate_gpa(report_card: dict[str, str]) -> float:
    points = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
    total = 0
    count = 0
    for grade in report_card.values():
        total += points[grade]
        count += 1
    return total / count


report_card = {
    "Math": "A",
    "Science": "C",
    "History": "A",
    "Art": "B",
    "English": "B",
    "Spanish": "A",
}
print(calculate_gpa(report_card))


# Problem 7: Best Book
def highest_rated(books: list[dict[str, str | float]]) -> dict[str, str | float]:
    best = books[0]
    for book in books:
        if float(book["rating"]) > float(best["rating"]):
            best = book
    return best


books = [
    {
        "title": "Tomorrow, and Tomorrow, and Tomorrow",
        "author": "Gabrielle Zevin",
        "rating": 4.18,
    },
    {
        "title": "A Fortune For Your Disaster",
        "author": "Hanif Abdurraqib",
        "rating": 4.47,
    },
    {
        "title": "The Seven Husbands of Evenlyn Hugo",
        "author": "Taylor Jenkins Reid",
        "rating": 4.40,
    },
]

print(highest_rated(books))


# Problem 8: Index-Value Map
def index_to_value_map(lst: list[str]) -> dict[int, str]:
    d = {}
    for i in range(len(lst)):
        d[i] = lst[i]
    return d


lst = ["apple", "banana", "cherry"]
print(index_to_value_map(lst))
