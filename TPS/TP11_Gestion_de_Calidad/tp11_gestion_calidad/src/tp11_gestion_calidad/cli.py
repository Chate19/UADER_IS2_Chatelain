"""Console script for tp11_gestion_calidad."""

import typer
from rich.console import Console

from tp11_gestion_calidad import utils

app = typer.Typer()
console = Console()


@app.command()
def main() -> None:
    """Console script for tp11_gestion_calidad."""
    console.print("Replace this message by putting your code into tp11_gestion_calidad.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
