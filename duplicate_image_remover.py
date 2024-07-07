import os
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


# Example usage
duplicates = find_duplicates('./samantha prabhu')
for dup in duplicates:
    os.remove(dup)

print("Duplicate images removed successfully.")
