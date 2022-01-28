import os
import time
import typer
from imggen.accessorygen.accessory_gen import *
from imggen.accessorygen.all_accessories import *
from imggen.colorgen.colors import *
from imggen.imgprocessing.img_generator import *
from imggen.imgprocessing.img_layering import *
from imggen.imgprocessing.opentemplate import *
from imggen.dirGen.makeIMGsDir import *
from imggen.args.progressbar.progressbar import *
from imggen.args.openImg.openImg import *

def main_loop(
    num_of_images: int,
    bar: bool=typer.Option(False, help="Show progress bar when generating images"),
    show: bool=typer.Option(False, help="Open image folder on completion")
):
    """
    main loop which generates the requested number of images
    """
    PATH = makeIMGsDir()

    loop_counter = num_of_images

    im = openTemplate()

    # things needed for progress bar to work
    bar_counter = 0

    # takes the starting time
    start_time = time.time()

    # main loop
    for i in range(0, loop_counter):

        BC, BG = color_gen()

        img_data = img_generator(BC, BG, im)

        hat_item, mouth_item, eye_item, body_item, hat_item_bool, mouth_item_bool, body_item_bool, eye_item_bool = accessory_gen()

        if hat_item_bool or mouth_item_bool or body_item_bool or eye_item_bool:
            img_layering(i ,img_data, PATH, hat_item, mouth_item, eye_item, body_item, hat_item_bool, mouth_item_bool, body_item_bool, eye_item_bool)

        img_data.save(f'{PATH}/duck-{i+1}.png')

        # progress bar
        if bar:
            bar_counter += 1
            if ((bar_counter/loop_counter)*30)%1 == 0:
                progressbar(bar_counter, loop_counter)


    # prints elapsed time to generate images rounded to 2 decimal places
    print(f'\nProcess finished -- {round(time.time()-start_time, 2)}s seconds --\n')

    if show:
        openImg(PATH)