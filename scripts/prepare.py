import glob
import json
import os
import shutil

from image import make_preview


def copy_products_data():
    print("Prepare products.json...")
    source = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.json')
    target = os.path.join(os.path.dirname(__file__), '..', 'public', 'data', 'products.json')

    shutil.copy(source, target)
    print("Products created in {}".format(target))

def extract_product_data():
    print("Prepare products.json...")
    source = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.json')
    target_dir = os.path.join(os.path.dirname(__file__), '..', 'public', 'data', 'products')

    with open(source, 'r') as f:
        json_data = f.read()
    
    data = json.loads(json_data)
    for item in data:
        target = os.path.join(target_dir, "{}.json".format(item['id']))
        with open(target, 'w') as f:
            f.write(json.dumps(item))
        print("Created data entry in {}".format(target))

def copy_categories_data():
    print("Prepare categories.json...")
    source = os.path.join(os.path.dirname(__file__), '..', 'data', 'categories.json')
    target = os.path.join(os.path.dirname(__file__), '..', 'public', 'data', 'categories.json')

    shutil.copy(source, target)
    print("Categories created in {}".format(target))

def create_description_json():
    source = os.path.join(os.path.dirname(__file__), '..', 'data', 'description.txt')
    target = os.path.join(os.path.dirname(__file__), '..', 'public', 'data', 'description.json')

    # copy contents of data/description.txt
    with open(source, 'r') as f:
        description_text = f.read()
    # turn it into json
    desc_json = {
        "description": description_text
    }
    # put it into public/data/description.json
    with open(target, 'w') as f:
        f.write(json.dumps(desc_json))

    print("Description JSON created")

def prepare_thumbnails():
    image_dirs_path = os.path.join(os.path.dirname(__file__), '..', 'public', 'products')
    image_dirs = glob.glob("{}/*/".format(image_dirs_path))

    for img_dir in image_dirs:
        print(img_dir)
        images = glob.glob("{}/*.jpg".format(img_dir))

        for image in images:
            if os.path.basename(image) != "1.jpg":
                continue
            dest = make_preview(image)
            print("Thumbnail Image: {}".format(dest))

if __name__ == '__main__':
    prepare_thumbnails()

    # copy_products_data()
    # extract_product_data()
    # copy_categories_data()
    # create_description_json()