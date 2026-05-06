# Problem 1: Is Monotonic
def is_monotonic(nums: list[int]) -> bool:
    inc = True
    dec = True
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            inc = False
        if nums[i] > nums[i - 1]:
            dec = False
    return inc or dec


nums1 = [1, 2, 2, 3, 10]
print(is_monotonic(nums1))

nums2 = [12, 9, 8, 3, 1]
print(is_monotonic(nums2))

nums3 = [1, 1, 1]
print(is_monotonic(nums3))

nums4 = [1, 9, 8, 3, 5]
print(is_monotonic(nums4))


# Problem 2: Student Directory
def student_directory(student_names: list[str]) -> dict[str, int]:
    d = {}
    for i in range(len(student_names)):
        d[student_names[i]] = i + 1
    return d


student_names = [
    "Ada Lovelace",
    "Tu Youyou",
    "Mae Jemison",
    "Rajeshwari Chatterjee",
    "Alan Turing",
]
print(student_directory(student_names))


# Problem 3: Dictionary Description
def get_description(info: dict[str, str], keys: list[str]) -> None:
    for key in keys:
        if key in info:
            print(info[key])
        else:
            print(None)


info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "occupation", "salary"]
get_description(info, keys)


# Problem 4: Sum Even Values
def sum_even_values(dictionary: dict[str, int]) -> int:
    total = 0
    for v in dictionary.values():
        if v % 2 == 0:
            total += v
    return total


dictionary = {"a": 4, "b": 1, "c": 2, "d": 8}
print(sum_even_values(dictionary))


# Problem 5: Merge Catalogs
def merge_catalogs(
    catalog1: dict[str, float], catalog2: dict[str, float]
) -> dict[str, float]:
    for k, v in catalog2.items():
        catalog1[k] = v
    return catalog1


catalog1 = {"apple": 1.0, "banana": 0.5}
catalog2 = {"banana": 0.75, "cherry": 1.25}
print(merge_catalogs(catalog1, catalog2))


# Problem 6: Items to Restock
def get_items_to_restock(products: dict[str, int], restock_threshold: int) -> list[str]:
    result = []
    for k, v in products.items():
        if v < restock_threshold:
            result.append(k)
    return result


products = {"Product1": 10, "Product2": 2, "Product3": 5, "Product4": 3}
restock_threshold = 5
print(get_items_to_restock(products, restock_threshold))


# Problem 7: Best Movie Genre
def most_popular_genre(movies: list[dict[str, str | float]]) -> str | None:
    totals = {}
    counts = {}
    for m in movies:
        g = m["genre"]
        r = m["rating"]
        if g in totals:
            totals[g] += r
            counts[g] += 1
        else:
            totals[g] = r
            counts[g] = 1
    best_genre = None
    best_avg = 0
    for g in totals:
        avg = totals[g] / counts[g]
        if avg > best_avg:
            best_avg = avg
            best_genre = g
    return best_genre


movies = [
    {"title": "Inception", "genre": "Science Fiction", "rating": 8.8},
    {"title": "The Matrix", "genre": "Science Fiction", "rating": 8.7},
    {"title": "Pride and Prejudice", "genre": "Romance", "rating": 7.8},
    {"title": "Sense and Sensibility", "genre": "Romance", "rating": 7.7},
]

print(most_popular_genre(movies))


# Problem 8: Quality Control
def quality_control(product_scores: dict[str, int], threshold: int) -> dict[str, str]:
    result = {}
    for k, v in product_scores.items():
        if v >= threshold:
            result[k] = "pass"
        else:
            result[k] = "fail"
    return result


product_scores = {"x0123": 75, "x0124": 40, "x0125": 90, "x0126": 55}
threshold = 60
print(quality_control(product_scores, threshold))
