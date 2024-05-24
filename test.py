def f(arr, i, n):
    if (i == n-1):
        return arr[i]
    
    if (i == 0):
        return ((arr[i] + f(arr, i+1,n )) / n)
    else:
        return (arr[i] + f(arr, i+1,n ))


list = [1,2,3]
#execute the function
print(f(list, 0, len(list))) # 2.0

