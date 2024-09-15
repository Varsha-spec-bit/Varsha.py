import os
import shutil

# Define the folder to organize
folder_path = "/path/to/your/folder"

# Define a dictionary for file categories based on extensions
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"],
    "Others": []
}

# Create folders for categories if they do not exist
def create_category_folders():
    for category in file_types.keys():
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

# Move files into categorized folders
def organize_files():
    for filename in os.listdir(folder_path):
        file_ext = os.path.splitext(filename)[1].lower()
        source_file = os.path.join(folder_path, filename)

        if os.path.isfile(source_file):
            moved = False
            for category, extensions in file_types.items():
                if file_ext in extensions:
                    dest_folder = os.path.join(folder_path, category)
                    shutil.move(source_file, dest_folder)
                    moved = True
                    break

            if not moved:
                others_folder = os.path.join(folder_path, "Others")
                shutil.move(source_file, others_folder)

# Main script
create_category_folders()
organize_files()
print("File organization completed!")
