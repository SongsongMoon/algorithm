import math


"""
1071 % 1029 => 42
y가 
"""
x = 10
y = 25
def gcd(x,y):
    if y > x:
        x, y = y, x

    while y:
        x,y = y, x%y
    return x

def gcd_recursive(x,y):
    if y > x:
        x,y = y,x
    
    if y == 0: 
        return x
    else:
        return gcd_recursive(y,x%y)

def lcm(x, y):
    return x * y // gcd(x,y)

print("GCD(%d,%d) = %d" %(x,y,gcd_recursive(x,y)))
print("LCM(%d,%d) = %d" %(x,y,lcm(x,y)))


#arr이 1개만 들어올 경우 조심
def lcm_list(arr):
    if len(arr) == 1:
        return arr[0]
        
    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]

def gcd_list(arr):
    if len(arr) == 1:
        return arr[0]

    while True:
        arr.append(gcd(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]


print(lcm_list([2,4]))
print(gcd_list([16,32,96]))