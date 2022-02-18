import json
from random import choices
import typer


app = typer.Typer()

def random_word_picker():
  '''
  Open words.json and pick a random word.
  '''

  words = None
  try:
    with open('words.json') as f:
      raw_words = f.read()
      words = json.loads(raw_words)
  except:
    print('An error has occured')


  random_word = choices(words)[0]

  return random_word


def draw_result(validation_status, user_guess):
  '''
  A function to print the resutlt in a stylish way
  '''

  status_grid = ''

  for idx, status in enumerate(validation_status):
    if status == 1:
      status_grid += f'{typer.style(" "+user_guess[idx]+" ", fg=typer.colors.WHITE, bg=typer.colors.GREEN, bold=True)} '
    elif status == 0:
      status_grid += f'{typer.style(" "+user_guess[idx]+" ", fg=typer.colors.WHITE, bg=typer.colors.YELLOW, bold=True)} '
    else:
      status_grid += f'{typer.style(" "+user_guess[idx]+" ", fg=typer.colors.BLACK, bg=typer.colors.WHITE, bold=True)} '

  status_grid += '\n'

  return status_grid


def validate(random_word, user_guess):
  ...


@app.command()
def main():
  ...


if __name__ == '__main__':
  app()