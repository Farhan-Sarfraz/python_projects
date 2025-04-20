def is_even(number):
    return number % 2 == 0

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def factorial(number):
    if number < 0:
        return "Not defined for negative numbers"
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result

def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))

def list_factors(number):
    return [i for i in range(1, number + 1) if number % i == 0]

def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

def is_armstrong(number):
    num_str = str(number)
    power = len(num_str)
    return number == sum(int(digit) ** power for digit in num_str)

# Main program
def number_analyzer():
    print(" Welcome to the Number Analyzer!")
    try:
        num = int(input("Enter an integer to analyze: "))
    except ValueError:
        print(" Please enter a valid integer.")
        return

    print("\n📋 Analysis Results:")
    print(f"1. Even or Odd: {'Even' if is_even(num) else 'Odd'}")
    print(f"2. Prime: {'Yes' if is_prime(num) else 'No'}")
    print(f"3. Factorial: {factorial(num)}")
    print(f"4. Sum of Digits: {sum_of_digits(num)}")
    print(f"5. Factors: {list_factors(num)}")
    print(f"6. Palindrome: {'Yes' if is_palindrome(num) else 'No'}")
    print(f"7. Armstrong Number: {'Yes' if is_armstrong(num) else 'No'}")

# Run the analyzer
if __name__ == "__main__":
    number_analyzer()
