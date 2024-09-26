import glob
import os

# Ganti path ini ke folder gambar.
image_dir_path = u'C:\\Users\\user\\Documents\\eirworks\\kaostalog\\WEB P'
def rename_image_files():
    if not os.path.exists(image_dir_path):
        print("Folder gambar tidak ditemukan")

    dirs = glob.glob(image_dir_path + "/*/")

    for img_dir in dirs:
        images = glob.glob(img_dir + "/*.jpg")
        # print(img_dir)

        i = 1
        for img in images:
            # print("|- {}".format(os.path.basename(img)))
            new_name = os.path.join(os.path.dirname(img), "{}.jpg".format(i))
            # print(new_name)
            os.rename(img, new_name)
            i += 1

if __name__ == '__main__':
    rename_image_files()