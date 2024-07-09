import os
import argparse
from PIL import Image
import imagehash


def find_duplicates(image_folder):
    image_hashes = {}
    duplicates = []

    for filename in os.listdir(image_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(image_folder, filename)
            image = Image.open(image_path)
            hash_value = imagehash.average_hash(image)

            if hash_value in image_hashes:
                duplicates.append(image_path)
            else:
                image_hashes[hash_value] = image_path

    return duplicates


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find and remove duplicate images in a folder.")
    parser.add_argument("-p", "--path", type=str, help="Path to the folder containing images.")

    args = parser.parse_args()
    image_folder = args.path

    duplicates = find_duplicates(image_folder)
    for dup in duplicates:
        os.remove(dup)

    print("Duplicate images removed successfully.")
