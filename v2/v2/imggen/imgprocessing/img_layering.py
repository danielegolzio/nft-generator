def img_layering(i, img_data, PATH, hat_item, mouth_item, eye_item, body_item, hat_item_bool, mouth_item_bool, body_item_bool, eye_item_bool):
    """
    Layers all of the generated accessories onto the base duck image
    """
    if hat_item_bool:
        img_data.paste(hat_item, (0,0), hat_item)
    if mouth_item_bool:
        img_data.paste(mouth_item, (0,0), mouth_item)
    if body_item_bool:
        img_data.paste(body_item, (0,0), body_item)
    if eye_item_bool:
        img_data.paste(eye_item, (0,0), eye_item)