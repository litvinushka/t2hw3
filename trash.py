import os
import shutil
import threading

def move_file(src_path, dest_path):
    shutil.move(src_path, dest_path)

def process_folder(folder_path, destination_folder):
    files = os.listdir(folder_path)

    for file in files:
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(file)
            dest_folder = os.path.join(destination_folder, file_extension[1:].lower())
            os.makedirs(dest_folder, exist_ok=True)

            dest_path = os.path.join(dest_folder, file)
            threading.Thread(target=move_file, args=(file_path, dest_path)).start()

        elif os.path.isdir(file_path):
            threading.Thread(target=process_folder, args=(file_path, destination_folder)).start()

def main():
    source_folder = "Хлам"
    destination_folder = "Відсортовано"

    os.makedirs(destination_folder, exist_ok=True)

    process_folder(source_folder, destination_folder)

if __name__ == "__main__":
    main()