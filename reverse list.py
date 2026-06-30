def reverse(n):
    
    reverse=n[::-1]
    return reverse
r=reverse(list(map(int, input('enter the numbers to make a list : ').split())))
print(r)