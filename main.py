"""Tex-based slot machine.
"""


def deposit() -> int:
    """Get the amount to be deposited by the player.

    Returns:
        int: amount deposited by player.
    """
    while True:
        amount = input("What would you like to deposit?")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number.")
    return amount
