# Part 1
def is_password(num):
    t = str(num)

    return (
        # has two adjacent digits
        any(x == y for x, y in zip(t, t[1:]))
        and
        # is non-decreasing
        all(int(x) <= int(y) for x, y in zip(t, t[1:]))
    )


start, end = 307237, 769058
print(sum(is_password(num) for num in range(start, end + 1)))

# Part 2
def is_password_two(num):
    from collections import Counter

    t = str(num)
    digits = Counter(t)

    return (
        (2 in digits.values())
        and
        # is non-decreasing
        all(int(x) <= int(y) for x, y in zip(t, t[1:]))
    )

start, end = 307237, 769058
print(sum(is_password_two(num) for num in range(start, end + 1)))