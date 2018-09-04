"""
Hex colours
"""


HEX_COLOURS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1": "#7fffd4",
               "azure1": "#f0ffff", "beige": "#f5f5dc", "black": "#000000"}
colour = input("Enter a colour name: ")
while colour != "":
    print(HEX_COLOURS.get(colour))
    colour = input("Enter a colour name: ")
