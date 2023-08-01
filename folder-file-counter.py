import os

def count_files_and_folders(folder_path):
    extension_count = {}
    folder_count = {}

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            _, extension = os.path.splitext(file)
            extension = extension[1:]
            extension_count[extension] = extension_count.get(extension, 0) + 1

        for folder in dirs:
            folder_path = os.path.join(root, folder)
            folder_count[folder_path] = count_files_and_folders(folder_path)

    return extension_count, folder_count

def save_to_file(file_path, extension_count, folder_count, indent=0):
    with open(file_path, 'w') as file:
        for extension, count in extension_count.items():
            file.write(f"{' ' * indent}{extension}: {count}\n")

        for folder, count in folder_count.items():
            if isinstance(count, tuple):
                file.write(f"{' ' * indent} folder: {os.path.basename(folder)}\n")
                save_to_file(file_path, *count, indent=indent + 2)
            else:
                file.write(f"{' ' * (indent + 2)} folder: {os.path.basename(folder)}\n")
                file.write(f"{' ' * (indent + 4)} Number of files: {count}\n")

if __name__ == "__main__":
    folder_path = input("Enter image file path: ")
    extension_count, folder_count = count_files_and_folders(folder_path)
    save_to_file("result.txt", extension_count, folder_count)
