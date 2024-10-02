import os
from PIL import Image

def make_preview(path_to_img: str) -> str:
    target_dir = os.path.dirname(path_to_img)
    target = os.path.join(target_dir, 'preview.jpg')
    size = (240, 240)

    if os.path.exists(target):
        os.remove(target)

    img = Image.open(path_to_img)
    img.thumbnail(size)
    img.save(target, "JPEG", quality=85)

    return target