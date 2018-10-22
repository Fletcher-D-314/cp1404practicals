import os
import shutil

DIRECTORY = "C:/Users/choos/OneDrive/Desktop/Pycharm Projects/cp1404practicals/prac_09"


def main():
    os.chdir('FilesToSort')
    extensions = []
    get_extensions(extensions)
    make_directory(extensions)
    move_files(extensions)


def get_extensions(extensions):
    for filename in os.listdir('.'):
        file = os.path.splitext(filename)
        extension = file[-1]
        if extension not in extensions:
            extensions.append(extension)


def make_directory(extensions):
    for extension in extensions:
        os.mkdir("{}/FilesToSort/{}".format(DIRECTORY, extension))


def move_files(extensions):
    for extension in extensions:
        os.chdir("{}/FilesToSort".format(DIRECTORY))
        for file in os.listdir("."):
            if file not in extensions:
                split = file.split(".")
                if extension == ".{}".format(split[-1]):
                    shutil.move(file, extension)


main()
