def number_analyzer():
    """
    Analyze a number: determine if it's even/odd, positive/negative/zero,
    and prime or not.
    """
       #--- INPUT VALIDATION ---
# Continuously ask until a valid interger is entered
    while True:
        try:
            num = int(input("Enter an integer: "))
            break  
        except ValueError:
            print("Invalid input! Please enter a whole number.")
# --- EVEN / ODD CHECK---
# Use modulo operator: if reminder is 0, it's even
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# --- SIGN CHECK ---
# Determine if the number is positive, negative, or 0
if num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print(f"{num} is zero (neither positive nor negative).")

# --- PRIME CHECK ---
# Prime numbers are greater than 1 and no divisors other than 1 and itself.
# we only need to check divisors up to the square root of the number.
if num > 1:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is prime.")
    else:
        print(f"{num} is not prime.")
else:
# numbers <= 1 are not prime
    print(f"{num} is not prime (prime numbers must be greater than 1).")
