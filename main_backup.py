"""Tex-based slot machine.
"""
MAX_LINES = 3


def deposit() -> int:
    """Get the amount to be deposited by the player.

    Returns:
        int: amount deposited by player.
    """
    while True:
        amount_input = input("What would you like to deposit? ")
        if amount_input.isdigit():
            amount = int(amount_input)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number.")
    return amount


def get_number_of_lines() -> int:
    """Get the number of lines to bet on.

    Returns:
        int: lines to bet on.
    """
    while True:
        lines_input = input(
            f"""How many lines would you like to bet on (1-{MAX_LINES})? """
        )
        if lines_input.isdigit():
            lines = int(lines_input)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines


def main() -> None:
    """main program"""
    balance: int = deposit()
    lines: int = get_number_of_lines()
    print(balance, lines)


main()
