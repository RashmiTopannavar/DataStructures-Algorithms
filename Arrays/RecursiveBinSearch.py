def recursive_bin_search(arr, low, high, key):
    if low <= high:
        mid = (low + high) // 2
        
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            return recursive_bin_search(arr, low, mid - 1, key)
        else:
            return recursive_bin_search(arr, mid + 1, high, key)
    
    return -1

# Test the function
if __name__ == "__main__":
    a = [2, 3, 5, 9, 11, 15, 18, 22, 25, 26, 30, 40]
    key = 2
    result = recursive_bin_search(a, 0, len(a) - 1, key)

    if result != -1:
        print(key, "is found at index", result)
    else:
        print("Key Not found")
