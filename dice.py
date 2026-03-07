import typer
import random
import sys
from rich import print
app = typer.Typer()
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
    if int(times) >= 2:
        print(f"You rolled a total of [bold green]{total}[/bold green]")
    sys.exit(0)
@app.command()
def help():
    typer.echo("How to roll dice: You use NdM notation aka Number of dice, dice, aMount of sides on dice \n \t How to roll using this cli: either run py -m dice roll * or if you added the .bat or .sh files to path respectively you can run dice roll * on windows and ./dice roll * on linux")

if __name__ == "__main__":
    app()
