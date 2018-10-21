import os


def main():
    os.chdir('FilesToSort')
    for filename in os.listdir():
        print(filename)