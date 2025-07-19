# YEEEEHEHEEEE =====PART II=====
# ----1
def prod(start, end):
    res = 1
    for i in range(min(start, end), max(start, end)+1):
        res *= i
    return res

print(prod(8, 1))

# ----2
def find_da_biggest_numbah(l):
    biggest_numbah = 0
    for i in l:
        if i > biggest_numbah:
            biggest_numbah = i
    return biggest_numbah

print(find_da_biggest_numbah([1, 2, 3, 4, 201012]))

# ----3
def summ(l):
    res = 0
    for i in l:
        res += i
    return res

print(summ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# ----4
def analyze(l):
    even = 0
    odd = 0
    pos = 0
    neg = 0
    for i in l:
        if i%2==0 and not i==0:
            even += 1
        elif i%2!=0:
            odd += 1
        if i > 0:
            pos += 1
        elif i<0:
            neg += 1
    return list([even, odd, pos, neg])
res = analyze([-4, -3, -2, -1, 0, 1, 2, 3, 4])

print(f"There are {res[0]} even numbers, {res[1]} odd numbers, {res[2]} positive numbers and {res[3]} negative numbers.")

#----5
def revlist(l):
    res = []
    for i in l[::-1]:
        res.append(i)
    return res

print(', '.join(map(str, revlist([1, 2, 5, 7, "%"]))))

# ----6
def map_factorials(l):
    reslist = []
    def factorial_recursive(n):
        if n == 0 or n == 1:
            return 1
        else:
            return  n * factorial_recursive(n-1)
    for i in l:
        reslist.append(factorial_recursive(i))
    return reslist

print(map_factorials([1, 2, 3, 4, 5]))        

# ----7
def generate_fibonacci(limit):
    res  = []
    a, b = 0, 1
    while b < limit:
        res.append(a+b)
        a, b = b, a + b
    return res

def check_fib(l):
    fib_ = generate_fibonacci(max(l))
    reslist = []
    for i in l:
        if i in fib_:
            reslist.append(i)
    return reslist

print(check_fib([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))

# =====PART III=====
# ----1
def volume(i, v):
    if v == 0:
        return 1
    else:
        return i * volume(i, v-1)
    
print(volume(2, 4))

# ----2
def return_sum(a, b, res=0, iteration=0):
    l = list(range(a, b+1))
    if iteration == len(l):
        return res if res == sum(l) else 0
    res += l[iteration]
    return return_sum(a, b, res, iteration + 1)

print(return_sum(1, 10))
"""As a result, 55 will be printed. Iteration is a variable I use to identify object by index. Then I add the object to RES and increase the iteration variable by 1."""

# ----3
def print_stars(length, iteration=0):
    if length == iteration:
        return 1
    else:
        print("*"*length)
        return print_stars(length, iteration+1)
        
print_stars(8)
