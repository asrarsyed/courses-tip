# Problem 1: Hello User!
def greet_user(name: str) -> None:
    print("Hello " + name)


greet_user("Michael")


# Problem 2: Calculate Difference
def difference(a: int, b: int) -> int:
    return a - b


diff = difference(8, 3)
print(diff)


# Problem 3: List Concatenation
def concatenate_list(nums: list[int]) -> list[int]:
    return nums + nums


print(concatenate_list([1, 2, 3, 4]))


# Problem 4: Sleep Assessment
def sleep_assessment(hours: int) -> None:
    if hours < 8:
        print("Oof, go back to bed!")
    elif hours <= 10:
        print("You got a good night's rest!")
    else:
        print("You're a sleep prodigy!")


sleep_assessment(10)
sleep_assessment(4)
sleep_assessment(12)
sleep_assessment(9)


# Problem 5: Calculate Tip
def calculate_tip(bill: float, service_quality: str) -> float | None:
    if service_quality == "poor":
        return bill * 0.10
    elif service_quality == "average":
        return bill * 0.15
    elif service_quality == "excellent":
        return bill * 0.20
    return None


tip1 = calculate_tip(44.53, "average")
print(tip1)
tip2 = calculate_tip(44.53, "poor")
print(tip2)
tip3 = calculate_tip(44.53, "excellent")
print(tip3)


# Problem 6: Rock, Paper, Scissors
def rock_paper_scissors(player1: str, player2: str) -> None:
    if player1 == player2:
        print("It's a tie!")
    elif (
        (player1 == "rock" and player2 == "scissors")
        or (player1 == "scissors" and player2 == "paper")
        or (player1 == "paper" and player2 == "rock")
    ):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


rock_paper_scissors("rock", "rock")
rock_paper_scissors("scissors", "rock")
rock_paper_scissors("scissors", "paper")
rock_paper_scissors("rock", "paper")
rock_paper_scissors("paper", "rock")


# Problem 7: Unscramble and Divide
def halve_lst(lst: list[float]) -> list[float]:
    result = []
    for number in lst:
        halved = number / 2
        result.append(halved)
    return result


print(halve_lst([2, 4, 6, 8]))


# Problem 8: Above the Threshold
def above_threshold(lst: list[int], threshold: int) -> list[int]:
    result = []
    for num in lst:
        if num > threshold:
            result.append(num)
    return result


lst = [8, 2, 13, 11, 4, 10, 14]
print(above_threshold(lst, 10))


# Problem 9: Countdown
def countdown(m: int, n: int) -> None:
    for i in range(m, n - 1, -1):
        print(i)


countdown(5, 1)


# Problem 10: Calculate Power
def power(base: int, exponent: int) -> int:
    result = 1
    for _ in range(exponent):
        result *= base
    return result


print(power(2, 5))
print(power(3, 3))


# Problem 11: Length of List
def list_length(lst: list[int]) -> int:
    count = 0
    for _ in lst:
        count += 1
    return count


lst = [2, 4, 6, 8, 10]
print(list_length(lst))


# Problem 12: Calculate Factorial
def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(3))


# Problem 13: Calculate the Squares
def squares(nums: list[int]) -> list[int]:
    result = []
    for num in nums:
        result.append(num * num)
    return result


print(squares([1, 2, 3, 4]))


# Problem 14: Multiply List
def multiply_list(lst: list[int], multiplier: int) -> list[int]:
    result = []
    for num in lst:
        result.append(num * multiplier)
    return result


lst = [1, 2, 3]
print(multiply_list(lst, 3))


# Problem 15: Count Evens
def count_evens(lst: list[int]) -> int:
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count


lst1 = [1, 5, 7, 9]
print(count_evens(lst1))

lst2 = [2, 4, 6, 8]
print(count_evens(lst2))
