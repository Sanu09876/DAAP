def karatsuba(x, y):
    # Base case: when the numbers are small enough (less than 10)
    if x < 10 or y < 10:
        return x * y
    
    # Find the size of the numbers
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    
    # Split the digit sequences in the middle
    high_x = x // 10**half
    low_x = x % 10**half
    high_y = y // 10**half
    low_y = y % 10**half
    
    # Recursive calls to karatsuba for smaller numbers
    z0 = karatsuba(low_x, low_y)  # Multiply the lower parts
    z1 = karatsuba(low_x + high_x, low_y + high_y)  # Multiply the sum of the parts
    z2 = karatsuba(high_x, high_y)  # Multiply the higher parts
    
    # Combine the results using the Karatsuba formula
    return (z2 * 10**(2 * half)) + ((z1 - z2 - z0) * 10**half) + z0

def square_large_number(n):
    # Use Karatsuba to square the number
    return karatsuba(n, n)

# Main program: Input a large number and compute its square
large_number = int(input("Enter a 20 digit number to square: "))
if len(str(large_number)) != 20 :
  print("Enter exactly 20 digit large number ")
else :
  result = square_large_number(large_number)
  print(f"Square of {large_number} is: {result}")

