def number_analyzer():
    """
    Analyze a number: determine if it's even/odd, positive/negative/zero,
    and prime or not.
    """
       # Get valid integer input from user
    while True:
        try:
            num = int(input("Enter an integer: "))
            break  # exit loop if conversion succeeded
        except ValueError:
            print("Invalid input! Please enter a whole number.")
# Check even or odd
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
# Determine sign (positive, negative, or zero)
if num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print(f"{num} is zero (neither positive nor negative).")
# Check if the number is prime (only for numbers > 1)
if num > 1:
    is_prime = True
    # Check divisors from 2 up to the square root of num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is prime.")
    else:
        print(f"{num} is not prime.")
else:
    print(f"{num} is not prime (prime numbers must be greater than 1).")
