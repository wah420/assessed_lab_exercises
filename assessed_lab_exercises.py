def calculator(num1, num2, operator):
    result = None  # Default value for invalid cases

    if operator == "+":  # Check for addition
        result = num1 + num2

    elif operator == "-":  # Check for subtraction
        result = num1 - num2

    elif operator == "*":  # Check for multiplication
        result = num1 * num2

    elif operator == "/":  # Check for division
        if num2 == 0:  # Handle division by zero
            print("You cannot divide by zero")
            result = 0  # Return 0 instead of None
        else:
            result = num1 / num2  # Valid division

    elif operator == "%":  # Check for modulo
        if num2 == 0:  # Handle modulo by zero
            print("You cannot take modulo by zero")
            result = 0  # Return 0 for modulo by zero
        else:
            result = num1 % num2

    elif operator == ">":  # Check for greater than
        result = num1 > num2

    elif operator == ">=":  # Check for greater than or equal
        result = num1 >= num2

    elif operator == "<":  # Check for less than
        result = num1 < num2

    elif operator == "<=":  # Check for less than or equal
        result = num1 <= num2

    else:
        print("Invalid operator.")
        result = 0  # Return 0 for invalid operators

    return result  # Return the calculated result


def max_of_three(num1, num2, num3):
    """
    This function takes three integers as input and returns the maximum of the three given numbers.

    Parameters:
    num1 (int): The first number.
    num2 (int): The second number.
    num3 (int): The third number.

    Returns:
    int: The maximum of the three numbers.
    """
    # Hint: you are required to make use of maximum variable that is returned by the function below.
    # Complete your code implementation here...

    maximum = num1

    if num2 > num1:
        maximum = num2
    if num3 > maximum:
        maximum = num3

    return maximum

def winning_numbers(user_list, winning_list):
    """
    This function checks if the user's numbers match the predefined winning numbers.

    Parameters:
    user_list (list): A list of three integers representing the user's chosen numbers.
    winning_list (list): A list of integers representing the winning numbers.

    Returns:
    str: A string indicating the prize won:
        - "First" if all three numbers match the winning numbers.
        - "Second" if two numbers match the winning numbers.
        - "Third" if one number matches the winning numbers.
        - "No" if none of the numbers match the winning numbers.

    Example:
    --------
    winning_list = [5, 14, 17]
    user_list = [3, 5, 10]
    result = winning_numbers(user_list, winning_list)
    # Output: "Third" (since one number, 5, matches the winning numbers)

    user_list = [14, 5, 10]
    result = winning_numbers(user_list, winning_list)
    # Output: "Third" (since two numbers, 14 and 5, match the winning numbers)

    The function also prints a message indicating the prize won.
    """

    # Function implementation here ...
    matching = len(set(user_list) & set(winning_list))

    if matching == 3:
        prize = "First"
    elif matching == 2:
        prize = "Second"
    elif matching == 1:
        prize = "Third"
    else:
        prize = "No"
        
    # Print the result
    print(f"Congratulations, you won {prize} prize!")
    return prize

def are_anagrams(str1, str2):
    """
    This function checks if two strings are anagrams of each other.

    Parameters:
    ----------
    str1 : str
        The first string to be compared.
    str2 : str
        The second string to be compared.

    Returns:
    -------
    bool:
        Returns True if the two strings are anagrams, otherwise False.

    Example:
    --------
    are_anagrams("listen", "silent")  # Output: True
    are_anagrams("hello", "world")    # Output: False
    """

    # Function implementation here ...
    output = False

    if len(str1) != len(str2):
        output = False 
    else:
        str1 = str1.lower()
        str2 = str2.lower()

        sorted_str1 = ''.join(sorted(str1))
        sorted_str2 = ''.join(sorted(str2))

        if sorted_str1 == sorted_str2:
            output = True

    return output

def calculate_average(numbers):


    """
    This function calculates the average of a list of numbers using a for loop.

    Parameters:
    ----------
    numbers : list
        A list of numerical values (int or float).

    Returns:
    -------
    float:
        The average of the numbers in the list. If the list is empty, returns None.

    Example:
    --------
    calculate_average([10, 20, 30, 40, 50])  # Output: 30.0
    """
    
    # Function implementation here ...
    if len(numbers) == 0:
        return None
    
    total_sum = 0
    for num in numbers:
        total_sum += num
    
    average = total_sum/ len(numbers)

    return average

def calculate_weekly_pay(hours_worked):
    """
    Calculate the weekly pay for an employee based on the number of hours worked.
    
    Parameters:
    hours_worked (int): The total number of hours worked by the employee in a week.
    
    Returns:
    float: The total weekly pay.
    """
    regular_rate = 12  # £12 per hour for up to 35 hours
    overtime_rate = 18  # £18 per hour for hours worked beyond 35 hours
    standard_hours = 35  # Threshold for regular pay



    # Function implementation here ...
    if hours_worked < 0:
        return 0
    
    if hours_worked <= 35:
        total_pay = hours_worked * regular_rate

    else:
        regular_pay = 35 * regular_rate

        overtime_hours = hours_worked - 35
        overtime_pay = overtime_hours * overtime_rate

        total_pay = regular_pay + overtime_pay



    return total_pay


    """
    This function implements a number guessing game where the user has to guess a randomly generated number between 0 and 10.

    The function performs the following steps:
    1. Generates a random number between 0 and 10 (inclusive) that the user needs to guess.
    2. Continuously prompts the user to enter their guess.
    3. Compares the user's guess with the generated number and provides feedback:
       - If the guess is correct, it prints a congratulatory message and exits the loop.
       - If the guess is too low, it informs the user that their guess is too low.
       - If the guess is too high, it informs the user that their guess is too high.
    4. Repeats this process until the user correctly guesses the number.
    """
    import random    
    answer = random.randint(0, 10)  # Generate a random number between 0 and 10

    # Step 3: Start a loop to allow the user to keep guessing
    while True:
        # Step 4: Prompt the user for a guess
        guess = int(input("Guess a number between 0 and 10: "))

        # Step 5: Check if the guess is correct, too low, or too high
        if guess == answer:
            print(f"Right! The answer is {answer}")
            break  # Exit the loop since the guess is correct
        elif guess < answer:
            print(f"Your guess of {guess} is too low!")
        else:  # guess > answer
            print(f"Your guess of {guess} is too high!")

def is_prime(num):
    """Checks if a number is prime.

    Input:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:

    boolean = is_prime(5)   # returns True
    print(boolean)
    """
    import math
    output = True
    
    if num <= 1:
        output = False  
    elif num == 2:
        output = True  
    elif num % 2 == 0:
        output = False 
    else:
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                output = False  
                break  
    
    return output

    """
    Plays a Rock-Paper-Scissors game between the user and the computer.
    
    The user is prompted to enter 'rock', 'paper', or 'scissors'.
    The computer randomly chooses one of the three options.
    The winner is determined based on the standard rules of the game.
    The game continues until the user decides to quit by entering 'quit'.
    """
    import random
    while True:

        user_choice = input("Please choose between rock, paper, or scissors (or type 'quit' to exit): ").lower()

        if user_choice == 'quit':
            print("Now exiting the game")
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please choose between rock, paper, or scissors.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])

        print(f"You chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
        else:
            print("You lose!")

def sum_of_evens(min_value, max_value):
    
    """Find the sum of even numbers between two given numbers (inclusive).

    Args:
        min_value (int): Minimum number
        max_value (int): Maximum number

    Returns:
        total: sum of the even numbers between min_value and max_value

    Example:

    min_value = 10
    max_value = 13
    total = sum_of_evens(min_value, max_value)
    print(total) # total is 22.

    """



    # Function implementation here ...
    if min_value > max_value:
        return 0
    
    total = sum(num for num in range(min_value, max_value + 1) if num % 2 == 0)

    return total

def celsius_to_fahrenheit(celsius):

    
    fahrenheit = (9 / 5) * celsius + 32
    return fahrenheit

def decrypt_cypher_text(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        ascii_value = ord(char)
        decrypted_ascii = ascii_value - key
        decrypted_ascii = decrypted_ascii % 256
        decrypted_char = chr(decrypted_ascii)
        decrypted_text += decrypted_char
    
    return decrypted_text

def find_maximum_difference(a, b):

    min_a = min(a)
    max_a = max(a)
    min_b = min(b)
    max_b = max(b)
    
    diff1 = abs(max_a - min_b)  
    diff2 = abs(max_b - min_a)  
    
    maximum = max(diff1, diff2)
    return maximum

def fuel_cost(distance_miles):
    # Constants
    MPG = 50  
    LITERS_PER_GALLON = 4.5 
    PRICE_PER_LITER = 1.49 
    
    gallons_needed = distance_miles / MPG
    
    liters_needed = gallons_needed * LITERS_PER_GALLON
    
    total_cost = liters_needed * PRICE_PER_LITER
    
    return total_cost

def is_golden_number(n):

    if n <= 0 or n >= 1000:
        return False

    for a in range(1, n):
        b = n - a  
        if (a * b) % 1000 == 0:  
            return True  

    return False  

def km_to_miles(kilometers):

    if kilometers < 0:
        print("Please enter a positive number.")
        return None

    conversion_factor = 0.62
    miles = kilometers * conversion_factor
    return round(miles, 3)




def letter_occurrence(input_string):

    count = 0
    for char in input_string:
        if char == 'a' or char == 'A':
            count += 1
    return count

def annual_net_income(gross_salary):

    if gross_salary >= 45000:
        tax_rate = 0.50
    elif 30000 <= gross_salary < 45000:
        tax_rate = 0.30
    else: 
        tax_rate = 0.15

    net_salary = gross_salary * (1 - tax_rate)
    return net_salary
