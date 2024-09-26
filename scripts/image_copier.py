import glob
import os
import shutil
from image_renamer import image_dir_path

products_dir = os.path.join(os.path.dirname(__file__), '..', 'public', 'products')

def copy_images():
    """
    Skrip ini belum bisa bekerja dengan baik.
    """
    print(products_dir)
    if os.path.exists(products_dir):
        print("Dir ok!")
        shutil.copytree(image_dir_path, products_dir)
    else:
        print("Dir {} not exists!".format(products_dir))
    
if __name__ == '__main__':
    copy_images()