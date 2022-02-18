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
  '''
  Validate the user guessed word with the random word picked based on the rule.

    - if the current letter of the user guessed word is the same as the letter at 
      the same position in the random word picked, then status of that position is 1
    
    - if the current letter of the user guessed word is not the same as the letter at 
      the same position in the random word picked, but the letter exists in the random 
      word picked, then status of that position is 0
    
    - if the current letter of the user guessed word is not in the random word picked,
      then status of that position is -1
  '''

  status = [None for i in range(5)]

  for idx in range(5):
    if user_guess[idx] == random_word[idx]:
      status[idx] = 1
    elif user_guess[idx] in random_word:
      status[idx] = 0
    else:
      status[idx] = -1

  return status


@app.command()
def main():
  ...


if __name__ == '__main__':
  app()