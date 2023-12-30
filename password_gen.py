from typer import Option, Typer, echo

from src.password_maker import password_maker, readable_password

app = Typer()

# https://pravash-techie.medium.com/python-better-clis-with-typer-a8783fafec6c#:~:text=What%20is%20Typer,arguments%20from%20the%20underlying%20functions.


@app.command(name="gen")
def generate(
    length: int = Option(
        12, "--length", "--len", help="The length of the password", show_default=True
    ),
    no_special_characters: bool = Option(
        False, "--no-special-characters", "-nsc", help="Exclude special characters"
    ),
    no_numbers: bool = Option(False, "--no-numbers", "-nn", help="Exclude numbers"),
    count: int = Option(1, "--count", "-c", help="Number of passwords to generate"),
    readable: bool = Option(False, "--readable", "-r", help="Generate a readable password"),
):
    """
    Generate a random password.

    Args:
        length (int): The length of the password. Default is 10.
        no_special_characters (bool): Exclude special characters if True. Default is False.
        no_numbers (bool): Exclude numbers if True. Default is False.
    """
    # generate multiple passwords
    passwords = []

    if readable:
        for i in range(count):
            # generate a password using the readable_password function
            passwords = readable_password(
                length=length,
                special_characters=not no_special_characters,
                numbers=not no_numbers,
            )
            echo(f"Password {i+1}: {passwords}")

    else:
        for i in range(count):
            # generate a password using the password_maker function
            passwords.append(
                password_maker(
                    length=length,
                    special_characters=not no_special_characters,
                    numbers=not no_numbers,
                )
            )
            echo(f"Password {i+1}: {passwords[i]}")

    with open("generated_passwords.txt", "a") as f:
        for password in passwords:
            f.write(password + "\n")


@app.command()
def history():
    """
    Show the history of generated passwords.
    """
    if past_passwords:
        for password in past_passwords:
            echo(password)
    else:
        echo("No passwords generated yet.")


@app.command(name="clr")
def clear():
    """
    Clear the history of generated passwords.
    """
    with open("generated_passwords.txt", "w") as f:
        f.write("")

    echo("History cleared.")


if __name__ == "__main__":
    past_passwords = []
    with open("generated_passwords.txt", "r") as f:
        past_passwords = f.read().splitlines()

    app()
