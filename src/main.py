import typer
from password_maker import password_maker

app = typer.Typer()

# https://pravash-techie.medium.com/python-better-clis-with-typer-a8783fafec6c#:~:text=What%20is%20Typer,arguments%20from%20the%20underlying%20functions.


@app.command()
def password(
    length: int = typer.Option(10, help="The length of the password", show_default=True),
    no_special_characters: bool = typer.Option(
        False, "--no-special-characters", "-nsc", help="Exclude special characters"
    ),
    no_numbers: bool = typer.Option(False, "--no-numbers", "-nn", help="Exclude numbers"),
):
    """
    Generate a random password.

    Args:
        length (int): The length of the password. Default is 10.
        no_special_characters (bool): Exclude special characters if True. Default is False.
        no_numbers (bool): Exclude numbers if True. Default is False.
    """
    typer.echo(
        password_maker(
            length=length, special_characters=not no_special_characters, numbers=not no_numbers
        )
    )


if __name__ == "__main__":
    app()
