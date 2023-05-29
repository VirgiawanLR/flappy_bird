def array_product(arr):
    n = len(arr)
    arr_product = []
    for i in range(n):
        temp = 1
        for j in range(i):
            temp *= arr[j]
        for j in range(n-1, i, -1):
            temp *= arr[j]
        arr_product.append(temp)
    return arr_product


arr = [1, 2, 3, 4]
product = array_product(arr)
print(product)

