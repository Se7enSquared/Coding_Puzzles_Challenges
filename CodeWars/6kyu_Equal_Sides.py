def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return None

print(find_even_index([20,10,30,10,10,15,35]))