def binary_search(low,high,target):
    guesses = 0
    while low <= high:
        mid = (low + high) // 2
        guesses += 1
        if mid == target:
            return guesses 
        elif mid < target:
            low = mid + 1
        else:
            high = mid - 1 
            return -1 
        
secret_number = 42
max_guesses = binary_search(1,100,secret_number)
print(f'computer found the number in {max_guesses} guesses.')        