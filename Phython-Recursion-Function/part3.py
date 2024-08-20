# def name_args():
# 1. name_args — Accepts any number of named arguments and prints them in the pattern key : value one at a time.
def name_args(**list):
    for i in list.keys():
        print(f"{i}:{list[i]}")

name_args(name="Tom", height="4.7", gender="Male")


# 2. all_true — Returns True if all the elements in an iterable are true. Hint: there is an existing built-in function that could be very helpful here.
def all_true(x):
    return all(x)

my_list = ["big", "small", "medium"]
result = all_true(my_list)
print(result)


# 3. one_true — Returns True if one of the elements in an iterable is true. Hint: there is an existing built-in function that could be very helpful here
def one_true():
    mytuple = (0, 1, False)
    x = any(mytuple)
    print(x)

one_true()


# 4. recursive_factorial — Uses recursion to find the factorial of an integer.
def recursize_facotial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursize_facotial(n - 1)
    
print(recursize_facotial(5))


# 5. recursive_deduplicate — Recursively removes all adjacent duplicate letters from a string.
def recursive_deduplicate(str):
    if len(str) < 2:
        return str
    
    i = 0
    while i < len(str) - 1:
        if str[i] == str[i + 1]:
            # Find the end of the sequence of duplicatestr
            while i < len(str) - 1 and str[i] == str[i + 1]:
                i += 1
            # Recursively process the string with the duplicates removed
            return recursive_deduplicate(str[:i - (i + 1) + 1] + str[i + 1:])
        i += 1
    
    # If no adjacent duplicates are found, return the string as is
    return str

# Example usage
print(recursive_deduplicate("apple tree map"))  # Output should be an empty string




# 6. recursive_reverse — Uses recursion to reverse a string.
def recursive_reverse(str, i=0):
    if len(str) == 0:
        return ""
    elif i == len(str)-1:
        return str[0]
    else:
        return str[-1-i] + recursive_reverse(str, i+1)

print(recursive_reverse("aaaa"))
print(recursive_reverse("aaba"))
print(recursive_reverse("pool"))