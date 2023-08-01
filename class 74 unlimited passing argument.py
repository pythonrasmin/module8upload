def add (a,b):
    """
    return the total number
    """
    total = a + b
    return total
print(add(34,34))

def multifle_add(*args):
    total = 0
    for number in args:
        # total = total+number
        total += number
    return total
result = multifle_add(1,2,3,4,5,6,7,8,9,10,11,12,13)
print(result)
