# checks for the symbol used to return an indicator for what function the main function should call
def check_func(nums):
    operation = None
    input_list = list(nums)

    # works backwards through the list, mainly for more optimal contrast between sub, double, and normal factorials.
    # it's put into a list so that it's more easily mutable
    # starting point has a -1 and end is -1 because of how list indexes and ranges work
    for digit in range(len(input_list) - 1, -1, -1):
        if input_list[digit] == "!":
            if input_list[digit - 1] == "!":
                operation = "double"
                break
            elif digit == 0:
                operation = "sub"
                break
            else:
                operation = "factorial"
                break
        elif input_list[digit] == "#":
            operation = "primorial"
            break
        elif input_list[digit] == "$":
            operation = "exponential"
            break
        elif input_list[digit] == "H":
            operation = "hyper"
            break
        elif input_list[digit] == "s":
            if input_list[digit + 1] == "f":
                operation = "sloane"
                break

    return operation


# just removes all non-integer string values and then joins it back into a string. it is made an int type in main
def num_isolator(nums):
    input_list = list(nums)
    running = True

    while running is True:
        if len(input_list) == 0:
            nums = -1
            return nums

        for digit in range(len(input_list)):
            try:
                int(input_list[digit])
                if digit == len(input_list) - 1:
                    running = False
                    break

            # broad except because there is only one outcome i want for any error that may occur for try
            except:
                input_list.pop(digit)
                break

    nums = "".join(input_list)
    return nums


# nice recursive function for calculating a factorial. is reused a lot later.
def factorial(arg):
    if arg == 0:
        return 1
    else:
        return arg * factorial(arg - 1)


# essentially just calculates the summation part of a subfactorial
# called sigma because i was going to make a separate function for multiplying n! with the summation, but
# too redundant and ended up just multiplying in n! in the print statement found in main
def sigma(arg):
    if arg == 2:
        return 1/2
    else:
        if arg % 2 == 1:
            return (-1/factorial(arg)) + sigma(arg - 1)
        elif arg % 2 == 0:
            return (1/factorial(arg)) + sigma(arg - 1)


# another recursive function with similar logic to factorial(), but with - 2 to skip numbers and a catch for both 1 + 0
def double_factorial(arg):
    if arg == 0 or arg == 1:
        return 1
    else:
        return arg * double_factorial(arg - 2)


# another recursive function to more easily get the job done. nested recursive function!!!
def super_factorial(arg):
    if arg == 0:
        return 1
    else:
        return factorial(arg) * super_factorial(arg - 1)


# making this a seperate function proved to make calculating the primorial much simpler to code
def is_prime(arg):
    prime = True

    for div in range(2, arg):
        if arg % div == 0:
            prime = False

    return prime


# similar logic to factorial(); only multiplies together if arg is a prime
def primorial(arg):
    if arg == 0:
        return 1
    elif is_prime(arg) is False:
        return primorial(arg - 1)
    elif is_prime(arg) is True:
        return arg * primorial(arg - 1)


# another fun recursive funciton
def expo_factorial(arg):
    if arg == 0:
        return 1
    else:
        return arg ** expo_factorial(arg - 1)


# and again
def hyper_factorial(arg):
    if arg == 0:
        return 1
    else:
        return (arg ** arg) * hyper_factorial(arg - 1)


def main():
    nums = ""

    print(
        "\n\nWelcome to the Ultimate Factorial Calculator!!\n"
        "---------------------------------------------\n"
        "Here are some useful symbols to help utilize the power of the UFC, where n is any integer:\n\n"
        "n!\n"
        "  - Factorial; multiply n by every integer before it until 1\n"
        "  - Ex: 5! = 5 * 4 * 3 * 2 * 1 = 120\n"
        "n!!\n"
        "  - Double Factorial; like a normal factorial but skips every other integer\n"
        "  - Ex: 7!! = 7 * 5 * 3 * 1 = 105\n\n"
        "!n\n"
        "  - Subfactorial; n! multiplied by the sum from 1 to n of (-1)^n * 1/(n!)\n"
        "  - Ex: !4 = 4!(1 - 1/1! + 1/2! - 1/3! + 1/4!) = 24(3/8) = 9\n\n"
        "n#\n"
        "  - Primorial; like a normal factorial but only including prime numbers\n"
        "  - Ex: 7# = 7 * 5 * 3 * 2 = 210\n\n"
        "n$\n"
        "  - Exponential Factorial; n^(n-1)^(n-2)^...^1\n"
        "  - Ex: 4$ = 4^3^2^1 = 4^9 = 262144\n\n"
        "sf(n)\n"
        "DISCLAIMER: This is sloane's definition. The other, Pickover's definition, grows too rapidly to be practical.\n"
        "  - Super Factorial; like a factorial, but the factorial of every factor\n"
        "  - n! * (n-1)! * (n-2)! * ... * 1\n"
        "  - Ex: sf(4) = 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288\n"
        "H(n)\n"
        "  - Hyper Factorial; n^n * (n-1)^(n-1) * ... * 1^1\n"
        "  - Ex: H(4) = 4^4 * 3^3 * 2^2 * 1^1 = 246 * 27 * 4 * 1 = 27648\n\n\n"
        "Type and enter 'exit' to quit the program.\n\n"
    )

    while nums != "exit":
        nums = input("Enter your factorial calculation: ")

        # inputting "exit" comes through as nums, and would have been difficult to integrate as the operation var
        # decided to just catch it as is and break for the user submitting "exit"
        if nums == "exit" or nums == "Exit" or nums == "EXIT":
            print("\n\nExiting...\n")
            break

        operation = check_func(nums)
        arg = int(num_isolator(nums))

        if operation == "factorial":
            print(factorial(arg))
            print()

        # here you can see that i just multiplied the two functions in the print statement. much simpler.
        elif operation == "sub":
            print(int(factorial(arg) * sigma(arg)))
            print()

        elif operation == "double":
            print(double_factorial(arg))
            print()

        elif operation == "sloane":
            print(super_factorial(arg))
            print()

        elif operation == "exponential":
            print(expo_factorial(arg))
            print()

        elif operation == "hyper":
            print(hyper_factorial(arg))
            print()

        elif operation == "primorial":
            print(primorial(arg))
            print()

        elif operation is None:
            print("Something unrecognized is in your expression...")
            print()


if __name__ == "__main__":
    main()
