from all_accessories import *
import random

hats = [
    christmas
]

mouth = [
    cigarette
]

eyes = [
    None
]

body = [
    gold_chain
]

funky = [
    'upsidedown'
]

def accessory_gen():
    hat_item = random.choice([True, False])
    mouth_item = random.choice([True, False])
    eye_item = random.choice([True, False])
    body_item = random.choice([True, False])
    funky_item = random.choice([True, False])
    
    if hat_item:
        random.choice(hats)
    elif mouth_item:
        random.choice(mouth)
    elif eye_item:
        random.choice(eyes)
    elif body_item:
        random.choice(body)
    elif funky_item:
        random.choice(funky)
        