def get_integer_input():
    """Gets an integer input from the user."""
    return int(input("Enter an integer: "))


def check_even_odd(number):
    """Returns whether a number is even or odd."""
    return "an Even Number" if number % 2 == 0 else "an Odd Number"


if __name__ == "__main__":
    result1 = get_integer_input()
    final_result1 = check_even_odd(result1)
    print(f"{result1} is {final_result1}.\n")

    result2 = get_integer_input()
    final_result2 = check_even_odd(result2)
    print(f"{result2} is {final_result2}.\n")
