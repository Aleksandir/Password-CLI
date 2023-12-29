from typer import Option, Typer, echo

from src.password_maker import password_maker

app = Typer()

# https://pravash-techie.medium.com/python-better-clis-with-typer-a8783fafec6c#:~:text=What%20is%20Typer,arguments%20from%20the%20underlying%20functions.


@app.command(name="gen")
def generate(
    length: int = Option(
        10, "--length", "--len", help="The length of the password", show_default=True
    ),
    no_special_characters: bool = Option(
        False, "--no-special-characters", "-nsc", help="Exclude special characters"
    ),
    no_numbers: bool = Option(False, "--no-numbers", "-nn", help="Exclude numbers"),
    count: int = Option(1, "--count", "-c", help="Number of passwords to generate"),
):
    """
    Generate a random password.

    Args:
        length (int): The length of the password. Default is 10.
        no_special_characters (bool): Exclude special characters if True. Default is False.
        no_numbers (bool): Exclude numbers if True. Default is False.
    """
    passwords = []
    for i in range(count):
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


if __name__ == "__main__":
    past_passwords = []
    with open("generated_passwords.txt", "r") as f:
        past_passwords = f.read().splitlines()

    app()
