import click


@click.command()
@click.argument("config", type=click.File())
@click.argument("my_list", nargs=-1)
@click.option("-l", "log_path")
@click.option("-v", "verbose", is_flag=True)
@click.option("--flag", "flag", default=False, help="Help message")
def main(config, my_list, log_path, force, verbose: bool):
    pass
