# =====PART II (1)
# ----1
def return_the_sum(start, end):
	return sum(list(range(min(start, end), max(start, end)+1)))

print(return_the_sum(1, 10))

# ----2
def multiply_the_list(lis):
	res = 1
	for i in lis:
		res *= i
	return res

print(multiply_the_list([1, 2, 3, 4, 5, 6, 7]))

# ----3
def find_minimum(l):
	res = 18446744073709551615
	for i in l:
		if i < res:
			res = i
	return res

print(find_minimum([-4, 500, 1, 177, 827, 22])) # -4

# ----4
def leave_prime(l):
	result_list = []
	for i in l:
		amount = 0
		for y in range(1, i + 1):
			if i % y == 0:
				amount += 1
		if amount == 2:
			result_list.append(i)
	return result_list


print(leave_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# ----5
reqList = []
element = None

while element != "EXIT_COMM":
    element = input("Enter the element of the list you want to add into the list (enter EXIT_COMM to leave)> ")
    reqList.append(element)

requestedElement = input("Enter the element you want to delete > ")

def print_how_much_del(l, x):
    count = l.count(x)
    while requestedElement in l:
        l.remove(x)
    return count

print(print_how_much_del(reqList, requestedElement))

# ----6
list1 = input("Enter the first list separated with \", \" > ").split(", ")
list2 = input("Enter the second list separated with \", \" > ").split(", ")

def conjure(*lists):
	reslist = []
	for list_element in lists:
		for item in list_element:
			if not item in reslist:
				if str(item).isdigit():
					reslist.append(int(item))
				else:
					reslist.append(item)
	return reslist

print(conjure(list1, list2))

# ----7
list1 = list(map(int, input("Enter the first list separated > ").split()))
exp = int(input("Enter the exponent > "))

def turn_into_product(list_param, exponent):
	reslist = []
	for item in list_param:
		reslist.append(item**exponent)
	return reslist

print(turn_into_product(list1, exp))
