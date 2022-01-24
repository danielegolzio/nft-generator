import os
import time
import typer
from imggen.accessorygen.accessory_gen import *
from imggen.accessorygen.all_accessories import *
from imggen.colorgen.colors import *
from imggen.imgprocessing.img_generator import *
from imggen.imgprocessing.img_layering import *
from imggen.dirGen.makeIMGsDir import *
from imggen.txtgen.txt_img_file import *


# main loop which generates the requested number of images
def main_loop(num_of_images: int):

    PATH = makeIMGsDir()

    data = txt_img_file()

    loop_counter = num_of_images

    # takes the starting time
    start_time = time.time()

    # things needed for progress bar to work
    bar_counter = 0
    bar_empty = "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
    bar_block = ""

    # main loop
    for i in range(0, loop_counter):

        PF, EW, EC, BC, OT, BG, BK = color_gen()

        img_data = img_generator(data, PF, EW, EC, BC, OT, BG, BK)

        hat_item, mouth_item, eye_item, body_item, hat_item_bool, mouth_item_bool, body_item_bool, eye_item_bool = accessory_gen()

        if hat_item_bool or mouth_item_bool or body_item_bool or eye_item_bool:
            img_layering(i ,img_data, PATH, hat_item, mouth_item, eye_item, body_item, hat_item_bool, mouth_item_bool, body_item_bool, eye_item_bool)

        img_data.save(f'{PATH}/duck-{i+1}.png')

        # progress bar
        bar_counter += 1
        bar_block = ("█"*(round(int((bar_counter/loop_counter)*30), 1)))
        os.system('cls' if os.name == 'nt' else 'clear')
        typer.secho("|-" + bar_block + (bar_empty[len(bar_block)::]) + f"-| [{bar_counter}/{loop_counter}] [{int((bar_counter/loop_counter)*100)}%]")

    # prints elapsed time to generate images rounded to 2 decimal places
    print(f'\nProcess finished -- {round(time.time()-start_time, 2)}s seconds --\n')


if __name__ == '__main__':
    typer.run(main_loop)