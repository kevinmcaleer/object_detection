import os
import random
import shutil

def split_dataset(image_dir, label_dir, output_dir, train_ratio=0.8):
    # Create output directories for train and validation sets
    train_image_dir = os.path.join(output_dir, 'images', 'train')
    val_image_dir = os.path.join(output_dir, 'images', 'val')
    train_label_dir = os.path.join(output_dir, 'labels', 'train')
    val_label_dir = os.path.join(output_dir, 'labels', 'val')

    os.makedirs(train_image_dir, exist_ok=True)
    os.makedirs(val_image_dir, exist_ok=True)
    os.makedirs(train_label_dir, exist_ok=True)
    os.makedirs(val_label_dir, exist_ok=True)

    # Get a list of all image filenames (assuming .jpg/.jpeg/.png format)
    image_filenames = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]

    # Shuffle the dataset randomly
    random.shuffle(image_filenames)

    # Calculate the number of training samples
    num_train = int(len(image_filenames) * train_ratio)

    # Split the dataset into train and val sets
    train_images = image_filenames[:num_train]
    val_images = image_filenames[num_train:]

    # Copy train images and labels
    for image in train_images:
        # Move image file
        shutil.copy(os.path.join(image_dir, image), os.path.join(train_image_dir, image))

        # Move corresponding label file
        label_filename = image.replace('.jpg', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt')
        shutil.copy(os.path.join(label_dir, label_filename), os.path.join(train_label_dir, label_filename))

    # Copy val images and labels
    for image in val_images:
        # Move image file
        shutil.copy(os.path.join(image_dir, image), os.path.join(val_image_dir, image))

        # Move corresponding label file
        label_filename = image.replace('.jpg', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt')
        shutil.copy(os.path.join(label_dir, label_filename), os.path.join(val_label_dir, label_filename))

    print(f"Training set size: {len(train_images)}")
    print(f"Validation set size: {len(val_images)}")

# # Example usage:
# image_dir = '/path_to_your_dataset/images'
# label_dir = '/path_to_your_dataset/labels'
# output_dir = '/path_to_your_dataset/split_dataset'

# # Split with 80% training and 20% validation
# split_dataset(image_dir, label_dir, output_dir, train_ratio=0.8)
