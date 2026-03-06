import typer as tp
import random
from rich import print
app = tp.Typer()
@app.command()
def roll(dice_input: str):
    dice = dice_input.split("d")
    times = dice[0]
    dice = dice[1]
    rolled = 0
    total = 0
    for i in range(0, int(times)):
        rolled = random.randint(1, int(dice))
        total += rolled
        print(f"You rolled a [bold magenta]{rolled}[/bold magenta]")
    print(f"You rolled a total of [bold green]{total}[/bold green]")

if __name__ == "__main__":
    app()
