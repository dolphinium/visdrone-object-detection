import os
import random
import shutil

# Paths to the dataset folders
train_images_path = "data/VisDrone/VisDrone2019-DET-train/images"
train_annotations_path = "data/VisDrone/VisDrone2019-DET-train/annotations"

val_images_path = "data/VisDrone/VisDrone2019-DET-val/images"
val_annotations_path = "data/VisDrone/VisDrone2019-DET-val/annotations"

test_dev_images_path = "data/VisDrone/VisDrone2019-DET-test-dev/images"
test_dev_annotations_path = "data/VisDrone/VisDrone2019-DET-test-dev/annotations"

# Desired number of images for each set
desired_train_images = 500
desired_val_images = 100
desired_test_dev_images = 100

def reduce_dataset(images_path, annotations_path, desired_count):
    # Get the list of all image filenames
    image_filenames = [f for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))]
    print(f"Total images in {images_path}: {len(image_filenames)}")

    # Check if there are already fewer or the exact number of images needed
    if len(image_filenames) <= desired_count:
        print(f"No need to delete images in {images_path}, already less than or equal to desired count.")
        return

    # Randomly shuffle and select the filenames to keep
    random.shuffle(image_filenames)
    images_to_keep = set(image_filenames[:desired_count])

    # Delete the excess images and their corresponding annotations
    for image_filename in image_filenames:
        if image_filename not in images_to_keep:
            # Remove image file
            image_file_path = os.path.join(images_path, image_filename)
            os.remove(image_file_path)

            # Remove corresponding annotation file
            annotation_filename = os.path.splitext(image_filename)[0] + '.txt'  # Assuming annotation files have the same name as images
            annotation_file_path = os.path.join(annotations_path, annotation_filename)
            if os.path.exists(annotation_file_path):
                os.remove(annotation_file_path)

    print(f"Reduced {images_path} to {desired_count} images.")


# Reduce train, val, and test-dev datasets
reduce_dataset(train_images_path, train_annotations_path, desired_train_images)
reduce_dataset(val_images_path, val_annotations_path, desired_val_images)
reduce_dataset(test_dev_images_path, test_dev_annotations_path, desired_test_dev_images)

print("Dataset reduction complete.")