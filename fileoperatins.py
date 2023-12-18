import os
import shutil
import random

# Function to create a validation set
def create_validation_set(source_folder, validation_folder, percentage=20):
    # Create the validation folder if it doesn't exist
    if not os.path.exists(validation_folder):
        os.makedirs(validation_folder)

    # Iterate through each class folder (e.g., leafname_healthy, leafname_diseased)
    for class_folder in os.listdir(source_folder):
        class_path = os.path.join(source_folder, class_folder)

        # Skip if it's not a directory
        if not os.path.isdir(class_path):
            continue

        # Create the corresponding validation class folder
        validation_class_path = os.path.join(validation_folder, class_folder)
        if not os.path.exists(validation_class_path):
            os.makedirs(validation_class_path)

        # Get a list of images in the class folder
        images = os.listdir(class_path)

        # Calculate the number of images to move to the validation set
        num_validation_images = int(len(images) * (percentage / 100))

        # Randomly select images for the validation set
        validation_images = random.sample(images, num_validation_images)

        # Move selected images to the validation set folder
        for image in validation_images:
            source_path = os.path.join(class_path, image)
            destination_path = os.path.join(validation_class_path, image)
            shutil.move(source_path, destination_path)

# Example usage
source_folder = "D:/scripts/ranvi/plants/dataset"
validation_folder = "D:/scripts/ranvi/plants/validation"

create_validation_set(source_folder, validation_folder, percentage=20)
