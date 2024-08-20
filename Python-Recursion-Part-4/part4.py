# 1. Write a Python function called max_num()to find the maximum of three numbers.
def max_num():
    x = max(5, 10, 15)
    print(x)

max_num()

# 2.Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list():
    x = 5 * 10 * 2
    print(x)

mult_list()


# 3.Write a Python function called rev_string() to reverse a string.
def rev_string():
    txt = "Hello World" [::-1]
    print(txt)

rev_string()


# 4.Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(x, y, z):
    min_value = y
    max_value = z
    if min_value <= x <= max_value:
        print("True")
    else:
        print("False")

num_within(7, 1, 5)
num_within(3, 2 ,4)
num_within(3, 1, 3)
num_within(10, 2, 5)

# 5.Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# def pascal(n):
def pascal(rows):
    triangle = []

    for i in range(rows):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i-1][j]

        triangle.append(row)

    for row in triangle:
        print(row)



pascal(5)
pascal(3)
pascal(8)