seats = [101, 105, 110, 115, 120, 125, 130, 135, 140]

seat = int(input("Enter your seat number: "))

# Iterative Binary Search
def iterative_search(seats, seat):
    low = 0
    high = len(seats) - 1

    while low <= high:
        mid = (low + high) // 2

        if seats[mid] == seat:
            return mid
        elif seats[mid] < seat:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Recursive Binary Search
def recursive_search(seats, low, high, seat):
    if low > high:
        return -1

    mid = (low + high) // 2

    if seats[mid] == seat:
        return mid
    elif seats[mid] < seat:
        return recursive_search(seats, mid + 1, high, seat)
    else:
        return recursive_search(seats, low, mid - 1, seat)


print("\nSorted Train Seats:", seats)

# Results
if iterative_search(seats, seat) != -1:
    print("Iterative Search: Seat found!")
else:
    print("Iterative Search: Seat not found.")

if recursive_search(seats, 0, len(seats) - 1, seat) != -1:
    print("Recursive Search: Seat found!")
else:
    print("Recursive Search: Seat not found.")