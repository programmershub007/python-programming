# Examples of recursive and iterative ways to calculate factorials

# Recursive method
def rec_fact(n):
    if n < 0:
        return "Please enter a value greater than or equal to 0"
    elif n == 0:
        return 1
    return n * rec_fact(n - 1)

# Iterative method
def itr_fact(n):
    if n < 0:
        return "Please enter a value greater than or equal to 0"
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

# Examples: 
# -----------------------
# print(str(itr_fact(5)))
# -----------------------
# '120'
# -----------------------
# print(str(rec_fact(4)))
# -----------------------
# '24'
# -----------------------
