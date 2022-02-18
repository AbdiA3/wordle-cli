import typer


def main(name: str):
  typer.echo(f'Hello {name}')


if __name __ == '__main__':
  typer.run(main)