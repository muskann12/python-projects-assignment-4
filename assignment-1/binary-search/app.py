def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print("List:", arr)
target = int(input("Enter number to search: "))

result = binary_search(arr, target)

if result != -1:
    print(f"✅ Number found at index {result}")
else:
    print("❌ Number not found in the list")
 