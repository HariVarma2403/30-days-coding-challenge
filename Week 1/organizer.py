import os
import shutil

source_folder = "test_folder"  # change later to Downloads

file_types = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3"],
}

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        moved = False

        for folder, extensions in file_types.items():
            for ext in extensions:
                if file.lower().endswith(ext):
                    dest = os.path.join(source_folder, folder)
                    os.makedirs(dest, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest, file))
                    moved = True
                    break
            if moved:
                break

        if not moved:
            others = os.path.join(source_folder, "Others")
            os.makedirs(others, exist_ok=True)
            shutil.move(file_path, os.path.join(others, file))

print("Files organized successfully!")
