import os
import shutil

def organize_files(directory):
    """
    Organizes files in the specified directory into folders by file type.

    Args:
        directory (str): The path to the directory to organize.
    """
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = filename.split('.')[-1]
            folder_name = os.path.join(directory, file_extension)

            # Create folder if it doesn't exist
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            # Move the file to the corresponding folder
            shutil.move(os.path.join(directory, filename), os.path.join(folder_name, filename))

if __name__ == "__main__":
    # Replace with the path to your directory
    organize_files('test_directory')
