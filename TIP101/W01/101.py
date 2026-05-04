# Problem 1: Hello World!
def hello_world() -> None:
    print("Hello world!")


hello_world()


# Problem 2: Today's Mood
def todays_mood() -> None:
    mood = "😌"
    print("Today's mood: " + mood)


todays_mood()


# Problem 3: Lunch Menu
def print_menu(menu: str) -> None:
    print("Lunch today is: " + menu)


print_menu("🍕")


# Problem 4: Sum of Two Integers
def sum(a: int, b: int) -> int:
    return a + b


first = sum(13, 27)
print(sum(first, first))


# Problem 5: Product of Two Integers
def product(a: int, b: int) -> int:
    return a * b


print(product(22, 7))


# Problem 6: Classify Age
def classify_age(age: int) -> str:
    if age < 18:
        return "child"
    return "adult"


print(classify_age(18))
print(classify_age(7))
print(classify_age(50))


# Problem 7: What time is it?
def what_time_is_it(hour: int) -> str:
    if hour == 2:
        return "taco time 🌮"
    if hour == 12:
        return "peanut butter jelly time 🥪"
    return "nap time 😴"


print(what_time_is_it(2))
print(what_time_is_it(7))
print(what_time_is_it(12))


# Problem 8: Blackjack
def blackjack(score: int) -> None:
    if score == 21:
        print("Blackjack!")
    elif score > 21:
        print("Bust!")
    elif score >= 17:
        print("Nice hand!")
    else:
        print("Hit me!")


blackjack(21)
blackjack(24)
blackjack(19)
blackjack(10)


# Problem 9: First Item
def get_first(lst: list[int]) -> int | None:
    if len(lst) == 0:
        return None
    return lst[0]


print(get_first([3, 1, 6, 7, 5]))


# Problem 10: Last Item
def get_last(lst: list[int]) -> int | None:
    if len(lst) == 0:
        return None
    return lst[-1]


print(get_last([3, 1, 6, 7, 5]))


# Problem 11: Counter
def counter(stop: int) -> None:
    for i in range(1, stop + 1):
        print(i)


counter(7)


# Problem 12: Sum 1 to 10
def sum_ten() -> int:
    total = 0
    for i in range(1, 11):
        total += i
    return total


print(sum_ten())


# Problem 13: Sum to stop
def sum_positive_range(stop: int) -> int:
    total = 0
    for i in range(1, stop + 1):
        total += i
    return total


print(sum_positive_range(6))


# Problem 14: Sum range
def sum_range(start: int, stop: int) -> int:
    total = 0
    for i in range(start, stop + 1):
        total += i
    return total


print(sum_range(3, 9))


# Problem 15: Negative numbers
def print_negatives(lst: list[int]) -> int | None:
    found = False
    for num in lst:
        if num < 0:
            print(num)
            found = True
    if not found:
        print("None")


print_negatives([3, -2, 2, 1, -5])
print_negatives([1, 2, 3, 4, 5])
