import hashlib

def get_image_hash(image_path):

    with open(image_path, "rb") as file:
        data = file.read()

    return hashlib.md5(data).hexdigest()