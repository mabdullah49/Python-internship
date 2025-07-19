import os
import shutil
import argparse
from colorama import init, Fore, Style

init(autoreset=True)

def organize_files(directory):
    if not os.path.isdir(directory):
        print(Fore.RED + "Error: Provided path is not a directory.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            ext = filename.split('.')[-1]
            folder = os.path.join(directory, ext)
            os.makedirs(folder, exist_ok=True)
            shutil.move(file_path, os.path.join(folder, filename))
            print(Fore.GREEN + f"Moved {filename} to {folder}/")

def main():
    parser = argparse.ArgumentParser(
        description='File Organizer CLI Tool - Sort files into folders by extension.'
    )
    parser.add_argument(
        'path',
        type=str,
        help='Path to the directory to organize'
    )

    args = parser.parse_args()
    organize_files(args.path)

if __name__ == '__main__':
    main()
