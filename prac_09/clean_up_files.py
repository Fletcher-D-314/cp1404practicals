"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    # TODO: Use exception handling to avoid the crash (just pass)

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    name = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = ""
    for i, char in enumerate(name):
        if char.islower():
            try:
                if name[i + 1].isupper():
                    new = char + "_"
                    new_name += new
                else:
                    new_name += char
            except IndexError:
                new_name += char
        elif char.isupper():
            try:
                if name[i + 1].isupper():
                    new = char + "_"
                    new_name += new
                else:
                    new_name += char
            except IndexError:
                new_name += char
        elif char.isalpha():
            try:
                if name[i + 1].isupper():
                    new = char + "_"
                    new_name += new
                else:
                    new_name += char
            except IndexError:
                new_name += char
        else:
            new_name += char
    return new_name.title()



def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(full_name, new_name)


# main()
demo_walk()
