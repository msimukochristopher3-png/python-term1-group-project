def number_analyzer():
    """
    Analyze a number: determine if it's even/odd, positive/negative/zero,
    and prime or not.
    """
    # --- INPUT VALIDATION ---
    # Continuously ask until a valid integer is entered
    while True:
        try:
            num = int(input("Enter an integer: "))
            break
        except ValueError:
            print("Invalid input! Please enter a whole number.")

    # --- EVEN / ODD CHECK ---
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

    # --- SIGN CHECK ---
    if num > 0:
        print(f"{num} is positive.")
    elif num < 0:
        print(f"{num} is negative.")
    else:
        print(f"{num} is zero (neither positive nor negative).")

    # --- PRIME CHECK ---
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
        print(f"{num} is not prime (prime numbers must be greater than 1).")

# Temporary call to test the function
if __name__ == "__main__":
    number_analyzer()
