import os
import typer

def progressbar():
    bar_counter += 1
    bar_block = ("█"*(round(int((bar_counter/loop_counter)*30), 1)))
    os.system('cls' if os.name == 'nt' else 'clear')
    typer.secho("|-" + bar_block + (bar_empty[len(bar_block)::]) + f"-| [{bar_counter}/{loop_counter}] [{int((bar_counter/loop_counter)*100)}%]")