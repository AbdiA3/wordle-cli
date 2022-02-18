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
  ...


def validate(random_word, user_guess):
  ...


@app.command()
def main():
  ...


if __name__ == '__main__':
  app()