import colorama

def calculadora(operator):

    while True:
        N1 = input("\nPlease enter a value: ")
        if not N1.lstrip('-').replace('.', '', 1).isdigit():
            print(colorama.Fore.RED + "[ Invalid input! ]" + colorama.Style.RESET_ALL)
        else:
            N1 = float(N1)
            break

    while True:
        N2 = input("Please enter a value: ")
        if not N2.lstrip('-').replace('.', '', 1).isdigit():
            print(colorama.Fore.RED + "[ Invalid input! ]" + colorama.Style.RESET_ALL)
        else:
            N2 = float(N2)
            break

    result = 0
    if operator == 1:
        result = N1 + N2
    elif operator == 2:
        result = N1 - N2
    elif operator == 3:
        result = N1 * N2
    else: result = N1 / N2

    print("Result: " + str(result))

print("\n    1 - Addition\n    2 - Subtraction\n    3 - Multiplication\n    4 - Division")
while True:
    operator = input("\nChoose an operation: ")
    if operator not in {"1", "2", "3", "4"}:
        print(colorama.Fore.RED + "[ Invalid input! ]" + colorama.Style.RESET_ALL)
    else:
        break
calculadora(int(operator))