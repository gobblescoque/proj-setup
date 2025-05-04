import typer

from .layout import srclayout

app = typer.Typer()
app.command()(srclayout)

if __name__ == "__main__":
    app()