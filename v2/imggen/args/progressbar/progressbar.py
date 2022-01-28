import os
import typer

bar_empty = "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
bar_block = ""

def progressbar(bar_counter, loop_counter):
    os.system('cls' if os.name == 'nt' else 'clear')
    bar_block = ("█"*(round(int((bar_counter/loop_counter)*30), 1)))
    typer.secho("|-" + bar_block + (bar_empty[len(bar_block)::]) + f"-| [{bar_counter}/{loop_counter}] [{int((bar_counter/loop_counter)*100)}%]")