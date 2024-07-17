import click


@click.group(short_help="file_uploader_js CLI.")
def file_uploader_js():
    """file_uploader_js CLI."""
    pass


@file_uploader_js.command()
@click.argument("name", default="file_uploader_js")
def command(name):
    """Docs."""
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [file_uploader_js]
