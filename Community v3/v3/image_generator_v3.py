import numpy as np
from PIL import Image
import cv2
import time


def accessorize(img, acc_path):
    accessory_category = ["hats", "mouth", "eyes", "body"]

    hats = ["none", "christmas", "back_cap"]
    mouth = ["none", "cigarette", "joint"]
    eyes = ["none", "head_bandana_red"]
    body = ["none", "gold_chain", "bow_tie"]

    accessories = accessory_category + ["none", "none"]
    choice = np.random.choice(accessories, 5, replace=False)

    for category in choice:
        if category != "none":
            selection = np.random.choice(eval(category))
            if selection != "none":
                acc_img = Image.open(f"{acc_path}/{selection}.png")
                img.paste(acc_img, (0, 0), acc_img)

    return img


def img_generator(fp, dimensions):
    img = cv2.imread(fp)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    rnd = np.random.randint(0, 255)
    hue = img_hsv[:, :, 0]
    hue = np.mod(hue + rnd, 255)
    img_hsv[:, :, 0] = hue

    img = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)
    img = Image.fromarray(img, "RGB")

    return img


# gets the user to input how many images they want generated
def image_num():
    # asks user how many images they want to make
    while True:
        try:
            loop_counter = int(input("How many images would you like to generate?: "))
            if loop_counter < 1:  # User entered value less than 1
                print("Number of images must be at least 1.")
            else:  # Value is an integer and greater than or equal to 1
                break
        except ValueError:
            print("Wrong input...")

    return loop_counter


# main loop which generates the requested number of images
def main_loop():
    PATH = "Images"
    ACCESSORY_PATH = "accessories"
    dimensions = (420, 420)

    # loop_counter = image_num()
    loop_counter = image_num()

    # takes the starting time
    start_time = time.time()

    # main loop
    fix = Image.open("template-images/duck_fixed.png")
    for i in range(0, loop_counter):
        img = img_generator("template-images/duck.png", dimensions)
        img.paste(fix, (0, 0), fix)
        img = accessorize(img, ACCESSORY_PATH)
        img = img.resize(dimensions, resample=0)
        img.save(f"{PATH}/duck-{i+1}.png")

    # prints elapsed time to generate images rounded to 2 decimal places
    print(f"Process finished --- {round(time.time()-start_time, 2)}s seconds ---")


if __name__ == "__main__":
    main_loop()
