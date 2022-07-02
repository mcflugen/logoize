import pathlib
import sys

import rich_click as click

from .api import logoize as logoize_


@click.command()
@click.version_option(package_name="logoize")
@click.option("--yes", is_flag=True, help="Do not prompt for confirmation")
@click.option("--output", "-o", type=click.Path(file_okay=True, dir_okay=False), default=None)
@click.option("--format", "-f", type=click.Choice(["png", "svg"]), default=None)
@click.option("--theme", "-t", type=click.Choice(["light", "dark"]), default="light")
@click.argument("words", type=str)
def logoize(yes, words, output, format, theme):
    if output is None:
        output = sys.stdout
    elif pathlib.Path(output).exists() and not yes:
        click.confirm("file exists, overwrite?", abort=True)
    logoize_(words.strip(), output, format=format, light=theme == "light")
