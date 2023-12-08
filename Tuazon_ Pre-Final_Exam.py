print("CS112: COMPUTER PROGRAMMING 1 - PRE- FINAL EXAM")
print("Created by : Nicole Shane P. Tuazon")
def is_prime(num):
    # Function to check if a number is prime
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


while True:
    # Get user input for the starting number
    start = int(input("Enter the starting number: "))

    # Check if the starting number is negative
    if start < 0:
        print("Enter a non-negative number.")
        continue

    # Get user input for the ending number
    end = int(input("Enter the ending number: "))

    # Check if the ending number is less than the starting number
    if end < start:
        print(f"Enter a number greater than {start}.")
        continue

    # Check if either the starting or ending number is 0 to terminate the program
    if start == 0 or end == 0:
        print("Program terminated.")
        break

    # Display prime numbers within the given range
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)
