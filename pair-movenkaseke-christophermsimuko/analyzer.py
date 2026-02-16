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
