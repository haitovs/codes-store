# This function generates numbers of a given length 'n'
# It uses a depth-first search (DFS) approach to generate all possible numbers
# 'prefix' is the current number being generated, and 'available_digits' are the digits that can be added to the 'prefix'
def generate_numbers(n, prefix="", available_digits="012"):
    # If the length of the 'prefix' is equal to 'n', it means that a number of length 'n' has been generated
    # In this case, the function yields the 'prefix' and returns
    if len(prefix) == n:
        yield prefix
        return

    # For each digit in 'available_digits', the function creates a new 'prefix' by adding the digit to the end of the current 'prefix'
    for digit in available_digits:
        new_prefix = prefix + digit
        # If the new 'prefix' does not contain any repeated substrings of length 2 or more, the function recursively calls itself with the new 'prefix'
        if not repeated_by_couple(new_prefix):
            yield from generate_numbers(n, new_prefix, available_digits)

# This function checks if a number contains any repeated substrings of length 2 or more
def repeated_by_couple(num):
    # It checks all possible substring lengths from 1 to half the length of the number
    for length in range(1, len(num) // 2 + 1):
        # It checks all possible starting positions for the substrings
        for i in range(len(num) - 2 * length + 1):
            # If it finds a repeated substring, it returns True
            if num[i : i + length] == num[i + length : i + 2 * length]:
                return True
    # If it does not find any repeated substrings, it returns False
    return False

# Example usage:
# The user is asked to enter the length of the number
n = int(input("Enter the length of the number: "))
# The function 'generate_numbers' is called with the entered length 'n'
# The resulting numbers are stored in the list 'valid_numbers'
valid_numbers = list(generate_numbers(n))
# The list of numbers is printed
print("Numbers not repeated by couple of length", n, ":", valid_numbers)