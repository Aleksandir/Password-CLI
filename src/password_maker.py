import json
import random
import string

# TODO: add readability to the password as an option


def password_maker(
    length: int = 10, special_characters: bool = True, numbers: bool = True, readable: bool = False
):
    """
    Generates a random password of specified length.

    Args:
        length (int): The length of the password (default is 10).
        special_characters (bool): Whether to include special characters in the password (default is True).
        numbers (bool): Whether to include numbers in the password (default is True).
        readable (bool): Whether to generate a readable password from a list of words (default is False).

    Returns:
        str: The generated password.
    """
    if readable:
        words = [
            "apple",
            "banana",
            "cherry",
            "date",
            "elderberry",
            "fig",
            "grape",
            "honeydew",
            "ice",
            "jackfruit",
            "kiwi",
            "lemon",
            "mango",
            "nectarine",
            "orange",
            "pineapple",
            "quince",
            "raspberry",
            "strawberry",
            "tangerine",
            "ugli",
            "victoria",
            "watermelon",
            "xigua",
            "yellow",
            "zucchini",
        ]
        password = "-".join(random.choice(words) for _ in range(length))
    else:
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


def readable_password(length: int = 12, special_characters: bool = True, numbers: bool = True):
    """
    Generates a readable password based on a list of words.

    Args:
        length (int): The desired length of the password. Default is 12.
        special_characters (bool): Whether to include special characters in the password. Default is True.
        numbers (bool): Whether to include numbers in the password. Default is True.

    Returns:
        str: The generated password.
    """
    substitutions = {"a": "@", "e": "3", "i": "!", "o": "0", "s": "$"}

    with open("words.json") as f:
        words = json.load(f)

    len3Words = words["words"]["3"]
    len4Words = words["words"]["4"]
    len5Words = words["words"]["5"]
    len6Words = words["words"]["6"]

    # Use greedy algorithm to generate a password from the longest words possible

    # Create a list of word lists, sorted by word length in descending order
    word_lists = [len6Words, len5Words, len4Words, len3Words]

    password_words = []
    for word_list in word_lists:
        word_length = len(word_list[0])  # All words in the list have the same length
        while length >= word_length:
            password_words.append(random.choice(word_list))
            length -= word_length

    # If there are remaining characters, fill them with random characters
    if length > 0:
        password_words.append("".join(random.choice(string.ascii_lowercase) for _ in range(length)))

    # Join the words with hyphens and return the password

    password = "-".join(password_words)

    # Replace some characters with special characters
    if special_characters:
        for char in substitutions:
            if char in password and random.random() < 0.5:
                password = password.replace(char, substitutions[char], 1)

    if numbers:
        for i in range(random.randint(1, 3)):
            password = password.replace(random.choice(password), str(random.randint(0, 9)), 2)

    return password


if __name__ == "__main__":
    print(f"Standard password: {password_maker()}")
    print(f"Password without special characters: {password_maker(special_characters=False)}")
    print(f"Password without numbers: {password_maker(numbers=False)}")
