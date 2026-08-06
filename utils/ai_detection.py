import os

def detect_plastic(image_path):

    filename = os.path.basename(image_path).lower()

    if "bottle" in filename:
        return "PET Bottle"

    elif "bag" in filename:
        return "Plastic Bag"

    elif "container" in filename:
        return "Food Container"

    elif "cup" in filename:
        return "Plastic Cup"

    elif "milk" in filename:
        return "Milk Bottle"

    else:
        return "Mixed Plastic"