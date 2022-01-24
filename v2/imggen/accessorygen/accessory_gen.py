import random
import numpy as np
from imggen.accessorygen.all_accessories import hats, eyes, mouth, body

# generates all the accessories that the duck will have
def accessory_gen():
    accessory_bool = np.random.choice([True, False], 1, p=[0.8, 0.2])
    
    if accessory_bool:
        hat_item_bool = random.choice([True, False])
        mouth_item_bool = random.choice([True, False])
        eye_item_bool = random.choice([True, False])
        body_item_bool = random.choice([True, False])

        if hat_item_bool:
            hat_item = random.choice(hats)
        else:
            hat_item = None

        if mouth_item_bool:
            mouth_item = random.choice(mouth)
        else:
            mouth_item = None

        if eye_item_bool:
            eye_item = random.choice(eyes)
        else:
            eye_item = None

        if body_item_bool:
            body_item = random.choice(body)
        else:
            body_item = None
    else:
        hat_item = None
        mouth_item = None
        eye_item = None
        body_item = None
        hat_item_bool = None
        mouth_item_bool = None
        eye_item_bool = None
        body_item_bool = None

    return hat_item, mouth_item, eye_item, body_item, hat_item_bool, mouth_item_bool, body_item_bool, eye_item_bool