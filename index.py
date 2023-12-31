# Write a Python function called max_num()to find the maximum of three numbers.


def max_num(
    a, b, c
):  # This is my first attempt without looking at my notes from class. :)
    if a >= b and a >= c:
        big1 = a
    if b >= a and b >= c:
        big1 = b
    if c >= a and c >= b:
        big1 = c
    print(f"The biggest number is: {big1}")


def max_num2(*args):  # This one is better because you can use more than 3 numbers! :)
    maximum = max(args)
    print(f"The biggest number is: {maximum}")


max_num(5, 9, 2)
max_num2(4, 9, 10)


# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(args):
    product = 1
    for num in args:
        product *= num
    print(f"The final product is: {product}")

my_list = [1, 2, 3, 4]
mult_list(my_list)


# Write a Python function called rev_string() to reverse a string.

def rev_string(string):
    string2 = string[::-1]
    print(f"{string} reversed is: {string2}")

rev_string("Hello World")


# Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(a, b, c):
    if a >= b and a <= c:
        print(f"TRUE!!! {a} does fall in the range from {b} to {c}")
    else:
        print(f"FALSE!!! {a} does NOT fall in the range from {b} to {c}")

num_within(9, 1, 10)


# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

def pascal(n):
    def calculate_pascal_value(row, col):
        if col == 0 or col == row:
            return 1
        return calculate_pascal_value(row - 1, col - 1) + calculate_pascal_value(row - 1, col)

    for i in range(n):
        for j in range(i + 1):
            print(calculate_pascal_value(i, j), end=" ")
        print()

pascal(5)
