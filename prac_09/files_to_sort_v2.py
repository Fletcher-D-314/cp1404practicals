import os
import shutil

DIRECTORY = "C:/Users/choos/OneDrive/Desktop/Pycharm Projects/cp1404practicals/prac_09"

def main():
    os.chdir('FilesToSort')
    extensions = []
    get_extensions(extensions)
    # make_directory(extensions)
    # move_files(extensions)

def get_extensions(extensions):
    for filename in os.listdir('.'):
        file = os.path.splitext(filename)
        extension = file[-1]
        if extension not in extensions:
            extensions.append(extension)