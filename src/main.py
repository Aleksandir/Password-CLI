import typer

app = typer.Typer()


@app.command()
def hello_world():
    """
    Prints 'hello world' to the console.
    """
    print("hello world")


# https://pravash-techie.medium.com/python-better-clis-with-typer-a8783fafec6c#:~:text=What%20is%20Typer,arguments%20from%20the%20underlying%20functions.
@app.command()
def hello(name):
    print(f"hello {name}")


@app.command()
def greet2(name: str = typer.Argument("world", help="The name to greet", show_default=True)):
    typer.echo(f"Hello, {name}!")


@app.command()
def backup(database: str, output_dir: str, force: bool = False):
    if force:
        typer.echo("Forced backup requested!")
    else:
        typer.echo("Regular backup requested.")
    typer.echo(f"Database: {database}")
    typer.echo(f"Output directory: {output_dir}")


if __name__ == "__main__":
    app()
