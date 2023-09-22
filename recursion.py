def recursion(n):
    if n ==1:
        return 1
    if n==0:
        return 0
    else:
        return (n* recursion(n-1))


number = 5
print(recursion(number))
