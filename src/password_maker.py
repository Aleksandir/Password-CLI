# password creater to take as arguments
# password length
# special characters (default true)
# numbers (default true)
# TODO: add readablity to the password as an option

import random
import string


def password_maker(length: int = 10, special_characters: bool = True, numbers: bool = True):
    """
    Generates a random password of specified length.

    Args:
        length (int): The length of the password (default is 10).
        special_characters (bool): Whether to include special characters in the password (default is True).
        numbers (bool): Whether to include numbers in the password (default is True).

    Returns:
        str: The generated password.
    """
    acceptable_characters = ""

    # add standard characters
    acceptable_characters += string.ascii_letters
    acceptable_characters += string.ascii_lowercase

    # add special characters
    if special_characters:
        acceptable_characters += string.punctuation

    # add numbers
    if numbers:
        acceptable_characters += string.digits

    password = ""
    for i in range(length):
        password += random.choice(acceptable_characters)

    return password


if __name__ == "__main__":
    print(f"Standard password: {password_maker()}")
    print(f"Password without special characters: {password_maker(special_characters=False)}")
    print(f"Password without numbers: {password_maker(numbers=False)}")
