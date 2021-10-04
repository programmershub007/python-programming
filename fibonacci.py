def fibonacci(n): # get fibonacci element number 'n'
  if n < 0:
    return "Please try a number greater than 0"
  if n == 0:
    return 0
  if n == 1:
    return 1
  return (fibonacci(n-1) + fibonacci(n-2))

# Example: 
# -------------------------
# print(str(fibonacci(10)))
# -------------------------
# '55'
# -------------------------
